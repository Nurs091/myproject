from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from .models import User, Ad, Category, AdImage, AdStatus, AdHistory, EmailVerification
from django.utils.translation import get_language_from_request

from .forms import AdForm
from .serializers import (
    AdSerializer, AdStatusSerializer, CategorySerializer,
    UserSerializer, RegisterSerializer, VerifyEmailSerializer
)
from .utils import send_verification_code

# ------------------------ Аутентификация ------------------------

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('home')

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

# ------------------------ Главная и категории ------------------------
from django.utils.translation import get_language
@login_required
def home(request):
    lang_code = get_language()
    ads = Ad.objects.exclude(status__is_hidden=True)
    query = request.GET.get('q')
    status = request.GET.get('status')
    city = request.GET.get('city')

    # Определяем язык из запроса
    lang_code = get_language_from_request(request)

    # Исправляем next_url: если английский и путь начинается с /ru/, убираем /ru
    current_path = request.path
    if lang_code == 'en' and current_path.startswith('/ru/'):
        next_url = current_path[3:] or '/'  # убираем /ru, оставляем / или путь без префикса
    else:
        next_url = current_path

    # Фильтрация объявлений
    if query:
        ads = ads.annotate(
            lower_title=Lower('title'),
            lower_description=Lower('description')
        ).filter(Q(lower_title__icontains=query) | Q(lower_description__icontains=query))

    if status:
        ads = ads.filter(status_id=5)
    if city:
        ads = ads.filter(city=city)

    paginator = Paginator(ads, 5)
    page_obj = paginator.get_page(request.GET.get('page'))
    moderation_status_id = 6  # замените на актуальный ID из вашей базы
    moderation_count = Ad.objects.filter(status_id=moderation_status_id).count() if request.user.is_moderator else 0


    return render(request, 'home.html', {
        'ads': page_obj,
        'categories': Category.objects.all(),
        'query': query,
        'status': status,
        'city': city,
        'moderation_count': moderation_count,
        'next_url': next_url,  # <-- передаём в шаблон
    })
    


@login_required
def category_ads(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    ads_list = Ad.objects.filter(category=category).exclude(status__name__in=["On moderation", "Sold"])
    query, status, city = map(request.GET.get, ('q', 'status', 'city'))

    if query:
        ads_list = ads_list.annotate(
            lower_title=Lower('title'),
            lower_description=Lower('description')
        ).filter(Q(lower_title__icontains=query) | Q(lower_description__icontains=query))
    if status:
        ads_list = ads_list.filter(status__name__iexact=status)
    if city:
        ads_list = ads_list.filter(city=city)

    paginator = Paginator(ads_list.order_by('-created_at'), 10)
    return render(request, 'category_ads.html', {
        'category': category,
        'ads': paginator.get_page(request.GET.get('page')),
        'categories': Category.objects.all(),
        'query': query,
        'status': status,
        'city': city,
    })

# ------------------------ Объявления ------------------------

@login_required
def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    recommended_ads = Ad.objects.filter(category=ad.category).exclude(id=ad.id).order_by('-created_at')[:6]
    return render(request, 'ad_details.html', {
        'ad': ad,
        'categories': Category.objects.all(),
        'recommended_ads': recommended_ads,
    })


@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.status = AdStatus.objects.filter(name="On moderation").first()
            ad.save()
            for image in request.FILES.getlist('images'):
                AdImage.objects.create(ad=ad, image=image)
            return redirect('home')
    else:
        form = AdForm()
    return render(request, 'create_ad.html', {'form': form, 'categories': Category.objects.all()})


@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, author=request.user)
    if request.method == 'POST':
        AdHistory.objects.create(ad=ad, title=ad.title, description=ad.description, price=ad.price)
        ad.title = request.POST['title']
        ad.description = request.POST['description']
        ad.price = request.POST['price']
        if status_id := request.POST.get('status'):
            ad.status = get_object_or_404(AdStatus, id=status_id)
        ad.save()

        AdImage.objects.filter(id__in=request.POST.getlist('delete_images')).delete()
        for image in request.FILES.getlist('images'):
            AdImage.objects.create(ad=ad, image=image)

        messages.success(request, 'Объявление успешно обновлено ✅')
        return redirect('ad_detail', ad_id=ad.id)

    return render(request, 'edit_ad.html', {'ad': ad, 'statuses': AdStatus.objects.all()})


@login_required
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.user != ad.author:
        raise Http404("Нельзя удалить чужое объявление.")
    ad.delete()
    return redirect('profile')


@login_required
def update_ad_status(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, author=request.user)
    if request.method == 'POST':
        AdHistory.objects.create(ad=ad, title=ad.title, description=ad.description, price=ad.price)
        ad.status = get_object_or_404(AdStatus, id=request.POST['status_id'])
        ad.save()
    return redirect('profile')


# ------------------------ Профиль и избранное ------------------------

@login_required
def user_profile(request):
    return render(request, 'profile.html', {
        'user_ads': Ad.objects.filter(author=request.user),
        'favorite_ads': Ad.objects.filter(favorite_users=request.user),
        'ad_statuses': AdStatus.objects.all()
    })


@login_required
def user_favorites(request):
    return render(request, 'profile.html', {
        'favorite_ads': Ad.objects.filter(favorite_users=request.user)
    })


@login_required
def add_to_favorites(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if ad.favorite_users.filter(id=request.user.id).exists():
        ad.favorite_users.remove(request.user)
    else:
        ad.favorite_users.add(request.user)
    return redirect('ad_detail', ad_id=ad.id)

# ------------------------ Модерация ------------------------

def is_moderator(user):
    return user.is_authenticated and user.is_moderator


@user_passes_test(is_moderator)
def moderation_panel(request):
    ads = Ad.objects.filter(status__name="On moderation").order_by('-created_at')
    paginator = Paginator(ads, 5)
    return render(request, 'moderation_panel.html', {'ads': paginator.get_page(request.GET.get('page'))})


@user_passes_test(is_moderator)
def approve_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    ad.status = AdStatus.objects.get(name="Active")
    ad.save()
    messages.success(request, f'Объявление "{ad.title}" одобрено.')
    return redirect('moderation_panel')


@user_passes_test(is_moderator)
def reject_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    ad.status = AdStatus.objects.get(name="Rejected")
    ad.save()
    messages.error(request, f'Объявление "{ad.title}" отклонено.')
    return redirect('moderation_panel')


@user_passes_test(is_moderator)
def moderation_ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'moderator_ad_detail.html', {'ad': ad})

# ------------------------ API Views ------------------------

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class AdStatusViewSet(viewsets.ModelViewSet):
    queryset = AdStatus.objects.all()
    serializer_class = AdStatusSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Код подтверждения отправлен на email'}, status=201)
        return Response(serializer.errors, status=400)


class VerifyEmailAPIView(APIView):
    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']
            try:
                verification = EmailVerification.objects.get(email=email, code=code)
                if verification.is_expired():
                    return Response({'error': 'Код истёк'}, status=400)
                user = User.objects.get(email=email)
                user.is_active = True
                user.save()
                login(request, user)
                verification.delete()
                return Response({'detail': 'Email подтверждён. Теперь можно войти.'}, status=200)
            except EmailVerification.DoesNotExist:
                return Response({'error': 'Неверный код'}, status=400)
        return Response(serializer.errors, status=400)
    

from django.shortcuts import render

def register_page(request):
    return render(request, 'register.html')


from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import PasswordResetCode
from .utils import generate_reset_code, send_password_reset_code

class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'forgot_password.html')

    def post(self, request):
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            code = generate_reset_code()
            PasswordResetCode.objects.create(email=email, code=code)
            send_password_reset_code(email, code)
            request.session['reset_email'] = email
            return redirect('verify_reset_code')
        messages.error(request, "Email not found")
        return redirect('forgot_password')


class VerifyResetCodeView(View):
    def get(self, request):
        return render(request, 'verify_reset_code.html')

    def post(self, request):
        code = request.POST.get('code')
        email = request.session.get('reset_email')
        if email and PasswordResetCode.objects.filter(email=email, code=code).exists():
            request.session['verified_reset_email'] = email
            return redirect('reset_password')
        messages.error(request, "Invalid code")
        return redirect('verify_reset_code')


class ResetPasswordView(View):
    def get(self, request):
        if not request.session.get('verified_reset_email'):
            return redirect('forgot_password')
        return render(request, 'reset_password.html')

    def post(self, request):
        email = request.session.get('verified_reset_email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('reset_password')

        user = User.objects.get(email=email)
        user.password = make_password(password1)
        user.save()

        # Cleanup session and codes
        PasswordResetCode.objects.filter(email=email).delete()
        request.session.pop('reset_email', None)
        request.session.pop('verified_reset_email', None)

        messages.success(request, "Password updated successfully. You can now log in.")
        return redirect('login')