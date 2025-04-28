from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower

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

# Представление для главной страницы (доступно только авторизованным пользователям)
from django.db.models import Q
from django.db.models.functions import Lower

@login_required
def home(request):
    ads = Ad.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('q')
    status = request.GET.get('status')

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

    paginator = Paginator(ads, 5)  # 5 объявлений на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'ads': page_obj,
        'categories': categories,
        'query': query,
        'status': status,
    })

    # Фильтрация по статусу
    status = request.GET.get('status')
    if status:
        ads = ads.filter(status__name__iexact=status)

    # Убираем фильтрацию по категории (если не нужна), иначе оставляем так:
    category_id = request.GET.get('category')
    if category_id:
        ads = ads.filter(category__id=category_id)

    # Пагинация
    paginator = Paginator(ads, 5)  # 5 объявлений на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'ads': page_obj,
        'categories': categories
    })


# Представление для отображения объявлений в категории
@login_required
def category_ads(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    ads_list = Ad.objects.filter(category=category)  # Получаем объявления по категории
    categories = Category.objects.all()  # Получаем все категории

    paginator = Paginator(ads_list, 10)  # Показываем по 10 объявлений на странице
    page_number = request.GET.get('page')
    ads = paginator.get_page(page_number)

    return render(request, 'category_ads.html', {'category': category, 'ads': ads, 'categories': categories})

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
    categories = Category.objects.all()  # Для выбора категории в форме
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')

        # Получаем изображения
        images = request.FILES.getlist('images')  # Получаем список файлов изображений

        if title and description and price and category_id:
            category = get_object_or_404(Category, id=category_id)

            # 👇 Найти статус "Active" автоматически
            active_status = AdStatus.objects.filter(name="Active").first()

            ad = Ad.objects.create(
                title=title,
                description=description,
                price=price,
                category=category,
                author=request.user,
                status=active_status  # 👉 Теперь новый статус
            )

            # Сохраняем изображения
            for image in images:
                AdImage.objects.create(
                    ad=ad,
                    image=image
                )

            return redirect('home')  # После создания объявления возвращаем на главную
    return render(request, 'create_ad.html', {'categories': categories})


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
def profile_view(request):
    # Логика для отображения профиля пользователя
    return render(request, 'profile.html')

@login_required
def message_cab(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    receiver = ad.author  # Получатель - это автор объявления

    return render(request, 'message_cab.html', {'ad': ad})

@login_required
def message_inbox(request):
    # Получаем все сообщения, полученные текущим пользователем
    received_messages = Message.objects.filter(receiver=request.user)
    
    # Получаем все сообщения, отправленные текущим пользователем
    sent_messages = Message.objects.filter(sender=request.user)

    return render(request, 'message_inbox.html', {
        'received_messages': received_messages,
        'sent_messages': sent_messages,
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
    ad = get_object_or_404(Ad, id=ad_id, author=request.user)  # Проверяем, что объявление принадлежит пользователю
    if request.method == 'POST':
        status_id = request.POST.get('status_id')
        status = get_object_or_404(AdStatus, id=status_id)
        ad.status = status
        ad.save()
    return redirect('profile')  # После обновления вернуться на страницу профиля

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

from .models import Ad, AdHistory, AdImage  # Убедись, что все модели импортированы

from django.shortcuts import redirect

@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, author=request.user)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_price = request.POST.get('price')

        # Сохраняем старую версию перед изменением
        AdHistory.objects.create(
            ad=ad,
            title=ad.title,
            description=ad.description,
            price=ad.price
        )

        ad.title = new_title
        ad.description = new_description
        ad.price = new_price
        ad.save()

        # Удаление выбранных фото
        delete_image_ids = request.POST.getlist('delete_images')
        if delete_image_ids:
            AdImage.objects.filter(id__in=delete_image_ids, ad=ad).delete()

        # Добавление новых фото
        new_images = request.FILES.getlist('images')
        for image in new_images:
            AdImage.objects.create(ad=ad, image=image)

        # После редактирования — переход на страницу объявления
        return redirect('ad_detail', ad_id=ad.id)

    return render(request, 'edit_ad.html', {'ad': ad})
