from django.contrib import admin
from modeltranslation.admin import TranslationAdmin  # <-- Импортируем TranslationAdmin
from .models import Category, Ad, User, AdStatus

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):  # наследуем от TranslationAdmin
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(AdStatus)
class AdStatusAdmin(TranslationAdmin):  # наследуем от TranslationAdmin, если используешь перевод
    list_display = ('name', 'description', 'is_hidden')
    list_editable = ('is_hidden',)
    search_fields = ('name',)
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):  # для Ad перевод не настраивали, поэтому оставляем ModelAdmin
    list_display = ('title', 'author', 'category', 'price', 'status', 'created_at')
    search_fields = ('title', 'author__username', 'category__name')
    list_filter = ('status', 'category', 'created_at')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_moderator', 'date_joined')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_moderator', 'date_joined')
