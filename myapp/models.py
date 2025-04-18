from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

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


class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="ad_images/")

    def __str__(self):
        return f"Image for {self.ad.title}"


# Create your models here.
