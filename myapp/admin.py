from django.contrib import admin
from .models import User, Category, Ad, AdImage

# Регистрируем кастомную модель пользователя в админке
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'phone', 'date_joined', 'is_active', 'is_staff')  # Используем email и другие поля
    search_fields = ('email', 'username', 'phone')  # Поиск по email, username, и phone
    list_filter = ('is_active', 'is_staff', 'date_joined')  # Фильтры для поиска
    ordering = ('-date_joined',)  # Сортировка по дате присоединения
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}), 
        ('Personal info', {'fields': ('phone',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}), 
        ('Important dates', {'fields': ('date_joined',)}),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Отображаем только название категории
    search_fields = ('name',)  # Поиск по имени
    ordering = ('name',)  # Сортировка по имени

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created_at', 'author')  # Показываем цену и автора
    list_filter = ('category', 'created_at', 'price')  # Фильтры по категории, дате и цене
    search_fields = ('title', 'description', 'author__username')  # Поиск по названию и описанию
    ordering = ('-created_at',)  # Сортировка по дате создания
    date_hierarchy = 'created_at'  # Возможность навигации по дате
    fields = ('title', 'description', 'price', 'category', 'author')  # Обязательные поля для отображения

    # Добавим обязательные поля
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['author'].queryset = User.objects.filter(is_active=True)  # Только активные пользователи
        form.base_fields['category'].queryset = Category.objects.all()  # Все категории
        return form

@admin.register(AdImage)
class AdImageAdmin(admin.ModelAdmin):
    list_display = ('ad', 'image')  # Показываем изображение и связанное с ним объявление
    search_fields = ('ad__title',)  # Поиск по заголовку объявления
    ordering = ('-ad__created_at',)  # Сортировка по дате создания объявления
    list_filter = ('ad__created_at',)  # Фильтрация по дате
