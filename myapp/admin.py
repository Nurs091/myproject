from django.contrib import admin
from .models import Category, Ad, User  # Импортируем нужные модели

# Регистрация модели Category в админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Отображаем поле name в списке категорий
    search_fields = ('name',)  # Добавляем поиск по имени категории

# Регистрация других моделей (например, Ad)
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'created_at')
    search_fields = ('title', 'author__username', 'category__name')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'date_joined')
