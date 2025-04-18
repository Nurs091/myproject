from django.contrib import admin
from .models import User, Category, Ad, AdImage

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  # Example fields, adjust to your model
    search_fields = ('username', 'email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Adjust as needed
    search_fields = ('name',)

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')  # Adjust to your model fields
    list_filter = ('category', 'created_at')
    search_fields = ('title',)

@admin.register(AdImage)
class AdImageAdmin(admin.ModelAdmin):
    list_display = ('ad', 'image')  # Adjust to your model fields
    search_fields = ('ad',)

    
# Register your models here.
