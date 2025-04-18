from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, AdForm  # Импортируем форму для объявления
from .models import User, Category, Ad  # Добавьте Category, чтобы работать с этой моделью
from django.contrib.auth import login, logout


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Неверные имя пользователя или пароль')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Можно сразу логинить, если хочешь
            return redirect('home')  # Или на 'login', если хочешь, чтобы он сам вошёл
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    categories = Category.objects.all()[:4]  # Показываем 4 категории
    ads = Ad.objects.all()  # Все объявления
    return render(request, 'home.html', {'categories': categories, 'ads': ads})


def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user  # Присваиваем текущего пользователя как автора
            ad.save()
            return redirect('home')  # После сохранения перенаправляем на главную страницу
    else:
        form = AdForm()

    return render(request, 'create_ad.html', {'form': form})
