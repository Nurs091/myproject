from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Импортируем свою модель, а не стандартную!
from .models import Ad, AdImage

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # <-- важно: твоя модель myapp.User
        fields = ['username', 'email', 'phone', 'password1', 'password2']  # Добавляем телефон

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'category']  # Все необходимые поля

class AdImageForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = ['image']
