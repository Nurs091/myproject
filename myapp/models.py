from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import random
import string
from datetime import timedelta

# Кастомизация модели пользователя, наследяя от AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=False, null=False, unique=True)
    is_moderator = models.BooleanField(default=False)  # <-- Добавляем это поле

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    favorite_users = models.ManyToManyField(User, related_name='favorite_ads', blank=True)
    status = models.ForeignKey('AdStatus', on_delete=models.SET_NULL, null=True, default=None)
    city = models.CharField(max_length=100, blank=True)
    language = models.CharField(
        max_length=2,
        choices=[('ru', 'Русский'), ('en', 'English')],
        default='ru',
        verbose_name='Язык объявления'
    )

    def __str__(self):
        return self.title

# Модель для изображений объявлений
class AdImage(models.Model):
    ad = models.ForeignKey(Ad, related_name="images", on_delete=models.CASCADE)  # Связь с объявлением
    image = models.ImageField(upload_to='ads/images/')  # Путь для загрузки изображений
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.ad.title}"

class AdStatus(models.Model):
    name = models.CharField(max_length=50)  # Название статуса, например "Активно", "Продано", "На модерации"
    description = models.TextField(blank=True)  # Описание статуса (опционально)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class AdHistory(models.Model):
    ad = models.ForeignKey('Ad', related_name='history', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"История для {self.ad.title} ({self.changed_at.strftime('%d.%m.%Y %H:%M')})"


class EmailVerification(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return (timezone.now() - self.created_at).seconds > 600  # 10 минут

    @staticmethod
    def generate_code():
        return ''.join(random.choices(string.digits, k=6))

    def __str__(self):
        return f"{self.email} — {self.code}"
    

class PasswordResetCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() < self.created_at + timedelta(minutes=15)