from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Ad, AdImage  # Корректный импорт
from django.utils.translation import gettext_lazy as _

# Форма регистрации пользователя
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A user with that phone number already exists.")
        return phone


# Форма создания объявления с выбором города
class AdForm(forms.ModelForm):
    CITY_CHOICES = [
        ('Almaty', _('Almaty')),
        ('Astana', _('Astana')),
        ('Shymkent', _('Shymkent')),
        ('Karaganda', _('Karaganda')),
        ('Aktau', _('Aktau')),
    ]

    city = forms.ChoiceField(
        choices=CITY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=_("City")
    )

    LANGUAGE_CHOICES = [
        ('ru', _('Russian')),
        ('en', _('English')),
    ]

    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=_("Language")
    )

    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'category', 'city', 'language']
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'price': _('Price'),
            'category': _('Category'),
        }

class AdImageForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = ['image']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A user with that phone number already exists.")
        return phone
    




