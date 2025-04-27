from django.contrib import admin
from .models import Category, Ad, User, AdImage  # Добавили AdImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'created_at')
    search_fields = ('title', 'author__username', 'category__name')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'date_joined')

@admin.register(AdImage)  # Регистрация AdImage
class AdImageAdmin(admin.ModelAdmin):
    list_display = ('ad', 'image', 'created_at')
