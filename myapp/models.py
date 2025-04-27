from django.db import models
from django.contrib.auth.models import AbstractUser

# Кастомизация модели пользователя, наследяя от AbstractUser
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)  # Дополнительное поле для телефона

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ad(models.Model):
    title = models.CharField(max_length=255)  # Заголовок
    description = models.TextField()  # Описание
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор объявления
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Категория

    def __str__(self):
        return self.title

# Модель для изображений объявлений
class AdImage(models.Model):
    ad = models.ForeignKey(Ad, related_name="images", on_delete=models.CASCADE)  # Связь с объявлением
    image = models.ImageField(upload_to='ads/images/')  # Путь для загрузки изображений
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.ad.title}"


