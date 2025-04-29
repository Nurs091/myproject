from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages

from .forms import AdForm



from .forms import CustomUserCreationForm
from .models import User, Ad, Category, AdImage, AdStatus, AdHistory


# Представление для регистрации
def register(request):
    if request.user.is_authenticated:  # Если пользователь уже авторизован
        return redirect('home')  # Перенаправляем на домашнюю страницу

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Можешь активировать пользователя сразу
            user.save()
            login(request, user)  # Логиним пользователя после регистрации
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Представление для входа пользователя
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')  # Если пользователь уже авторизован, перенаправляем на главную страницу

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Получаем пользователя
            login(request, user)  # Авторизуем пользователя
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Представление для выхода пользователя
def user_logout(request):
    logout(request)  # Выход пользователя
    return redirect('home')  # Перенаправление на главную страницу


@login_required
def home(request):
    ads = Ad.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('q')
    status = request.GET.get('status')
    city = request.GET.get('city')  # <-- добавляем получение города из запроса

    if query:
        ads = ads.annotate(
            lower_title=Lower('title'),
            lower_description=Lower('description')
        ).filter(
            Q(lower_title__icontains=query) |
            Q(lower_description__icontains=query)
        )

    if status:
        ads = ads.filter(status__name__iexact=status)

    if city:
        ads = ads.filter(city=city)  # <-- фильтрация по городу

    paginator = Paginator(ads, 5)  # 5 объявлений на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'ads': page_obj,
        'categories': categories,
        'query': query,
        'status': status,
        'city': city,  # <-- передаём city в шаблон, чтобы отмечать выбранное значение
    })


# Представление для отображения объявлений в категории
@login_required
def category_ads(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    ads_list = Ad.objects.filter(category=category)
    categories = Category.objects.all()

    # Получение GET-параметров
    query = request.GET.get('q')
    status = request.GET.get('status')
    city = request.GET.get('city')

    # Поиск
    if query:
        ads_list = ads_list.annotate(
            lower_title=Lower('title'),
            lower_description=Lower('description')
        ).filter(
            Q(lower_title__icontains=query) |
            Q(lower_description__icontains=query)
        )

    # Фильтрация по статусу
    if status:
        ads_list = ads_list.filter(status__name__iexact=status)

    # Фильтрация по городу
    if city:
        ads_list = ads_list.filter(city=city)

    # Пагинация
    paginator = Paginator(ads_list.order_by('-created_at'), 10)
    page_number = request.GET.get('page')
    ads = paginator.get_page(page_number)

    return render(request, 'category_ads.html', {
        'category': category,
        'ads': ads,
        'categories': categories,
        'query': query,
        'status': status,
        'city': city,
    })

# Представление для отображения подробностей об объявлении
@login_required
def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    categories = Category.objects.all()

    # Поиск похожих объявлений из той же категории, исключая текущее объявление
    recommended_ads = Ad.objects.filter(
        category=ad.category
    ).exclude(id=ad.id).order_by('-created_at')[:6]  # Ограничиваем до 6 объявлений

    return render(request, 'ad_details.html', {
        'ad': ad,
        'categories': categories,
        'recommended_ads': recommended_ads,
    })

# Представление для создания нового объявления
@login_required
def create_ad(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)  # Используем Django Form
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user

            # Найти статус "Active"
            active_status = AdStatus.objects.filter(name="Active").first()
            ad.status = active_status

            ad.save()

            # Сохраняем изображения
            images = request.FILES.getlist('images')
            for image in images:
                AdImage.objects.create(ad=ad, image=image)

            return redirect('home')
    else:
        form = AdForm()

    return render(request, 'create_ad.html', {
        'form': form,
        'categories': categories
    })


@login_required
def user_profile(request):
    # Получаем объявления пользователя
    user_ads = Ad.objects.filter(author=request.user)
    
    # Получаем избранные объявления пользователя
    favorite_ads = Ad.objects.filter(favorite_users=request.user)
    
    # Получаем ВСЕ статусы объявлений
    ad_statuses = AdStatus.objects.all()

    return render(request, 'profile.html', {
        'user_ads': user_ads,
        'favorite_ads': favorite_ads,
        'ad_statuses': ad_statuses,  # <-- теперь переменная определена
    })



@login_required
def user_favorites(request):
    # Получаем все избранные объявления текущего пользователя
    favorite_ads = Favorite.objects.filter(user=request.user)
    return render(request, 'profile.html', {'favorite_ads': favorite_ads})

@login_required
def add_to_favorites(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    # Проверяем, не добавлено ли объявление в избранное
    if ad.favorite_users.filter(id=request.user.id).exists():
        # Если да, удаляем его из избранного
        ad.favorite_users.remove(request.user)
        message = "Объявление удалено из избранного."
    else:
        # Если нет, добавляем его в избранное
        ad.favorite_users.add(request.user)
        message = "Объявление добавлено в избранное."

    return redirect('ad_detail', ad_id=ad.id)  # Перенаправляем обратно на страницу объявления

def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    
    # Проверка, что текущий пользователь является автором объявления
    if request.user != ad.author:
        raise Http404("Вы не можете удалить это объявление.")

    # Удаляем объявление
    ad.delete()
    
    # Перенаправляем пользователя на страницу профиля или главную
    return redirect('profile')  # Или 'home', если хотите перенаправить на главную страницу

@login_required
def update_ad_status(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, author=request.user)
    if request.method == 'POST':
        status_id = request.POST.get('status_id')
        status = get_object_or_404(AdStatus, id=status_id)

        # Сохраняем старую версию перед изменением!
        AdHistory.objects.create(
            ad=ad,
            title=ad.title,
            description=ad.description,
            price=ad.price
        )

        # Потом обновляем статус
        ad.status = status
        ad.save()

    return redirect('profile')


@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, author=request.user)
    statuses = AdStatus.objects.all()

    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_price = request.POST.get('price')
        new_status_id = request.POST.get('status')

        AdHistory.objects.create(
            ad=ad,
            title=ad.title,
            description=ad.description,
            price=ad.price
        )

        ad.title = new_title
        ad.description = new_description
        ad.price = new_price

        if new_status_id:
            ad.status = get_object_or_404(AdStatus, id=new_status_id)

        ad.save()

        delete_image_ids = request.POST.getlist('delete_images')
        if delete_image_ids:
            AdImage.objects.filter(id__in=delete_image_ids, ad=ad).delete()

        new_images = request.FILES.getlist('images')
        for image in new_images:
            AdImage.objects.create(ad=ad, image=image)

        # >>> Уведомка после сохранения
        messages.success(request, 'Объявление успешно обновлено ✅')

        return redirect('ad_detail', ad_id=ad.id)

    return render(request, 'edit_ad.html', {
        'ad': ad,
        'statuses': statuses,
    })

