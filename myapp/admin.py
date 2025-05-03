from django.contrib import admin
from .models import Category, Ad, User, AdStatus  # Импортируем все нужные модели

# Регистрация модели Category в админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Отображаем поле name в списке категорий
    search_fields = ('name',)  # Добавляем поиск по имени категории

# Регистрация модели AdStatus в админке
@admin.register(AdStatus)
class AdStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Показываем название и описание статуса
    search_fields = ('name',)  # Добавляем поиск по имени статуса

# Регистрация модели Ad в админке
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'status', 'created_at')  # Добавил status
    search_fields = ('title', 'author__username', 'category__name')
    list_filter = ('status', 'category', 'created_at')  # Фильтрация по статусу, категории и дате

# Регистрация модели User в админке
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_moderator', 'date_joined')  # добавили is_moderator
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_moderator', 'date_joined') 
