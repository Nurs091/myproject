from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Менеджер для пользовательской модели
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Создание и сохранение обычного пользователя с email и паролем.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)  # Хэширует пароль перед сохранением
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Создание и сохранение суперпользователя с email и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


# Кастомная модель пользователя
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Дополнительные поля
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Может ли этот пользователь заходить в админку

    USERNAME_FIELD = 'email'  # Для аутентификации будем использовать email
    REQUIRED_FIELDS = ['username']  # Поля для суперпользователя

    objects = UserManager()  # Используем менеджер для пользователя

    def __str__(self):
        return self.username


# Категория для объявления
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Объявление
class Ad(models.Model):
    title = models.CharField(max_length=255)  # Заголовок
    description = models.TextField()  # Описание
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор объявления
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Категория (разрешаем NULL)

    def __str__(self):
        return self.title


# Изображения для объявления
class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="ad_images/")

    def __str__(self):
        return f"Image for {self.ad.title}"
