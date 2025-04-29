from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Ad, AdImage  # Корректный импорт

# Форма регистрации пользователя
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # <-- Важно: своя модель User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

# Форма создания объявления с выбором города
class AdForm(forms.ModelForm):
    CITY_CHOICES = [
    ('Almaty', 'Almaty'),
    ('Astana', 'Astana'),
    ('Shymkent', 'Shymkent'),
    ('Karaganda', 'Karaganda'),
    ('Aktau', 'Aktau'),
]

    city = forms.ChoiceField(
        choices=CITY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'category', 'city']  # Обязательно добавляем city!

# Форма загрузки изображений для объявления
class AdImageForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = ['image']
