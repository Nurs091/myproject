from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator  # Импортируем Paginator для пагинации
from .forms import CustomUserCreationForm
from .models import User, Ad, Category, AdImage  # Импортируем также модель AdImage

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
@login_required
def home(request):
    ads = Ad.objects.all()  # Получаем все объявления
    categories = Category.objects.all()  # Получаем все категории

    # Пагинация
    paginator = Paginator(ads, 10)  # 10 объявлений на страницу
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-запроса
    page_obj = paginator.get_page(page_number)  # Получаем страницы

    return render(request, 'home.html', {'ads': page_obj, 'categories': categories})

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
    categories = Category.objects.all()  # Получаем все категории
    return render(request, 'ad_details.html', {'ad': ad, 'categories': categories})

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
            ad = Ad.objects.create(
                title=title,
                description=description,
                price=price,
                category=category,
                author=request.user  # Используем author, а не user
            )

            # Сохраняем изображения для объявления
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
    
    return render(request, 'profile.html', {
        'user_ads': user_ads,
        'favorite_ads': favorite_ads,
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


