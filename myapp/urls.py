from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Страница регистрации
    path('login/', views.user_login, name='login'),  # Страница входа
    path('logout/', views.user_logout, name='logout'),  # Выход из аккаунта
    path('', views.home, name='home'),  # Главная страница
    path('category/<int:category_id>/', views.category_ads, name='category_ads'),  # Страница с объявлениями категории
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),  # Страница с подробностями объявления
    path('create/', views.create_ad, name='create_ad'),  # Кнопка создания объявлений
    path('profile/', views.user_profile, name='profile'),  # Профиль пользователя
    path('message_inbox/', views.message_inbox, name='message_inbox'),
    path('message_cab/<int:ad_id>/', views.message_cab, name='message_cab'),
    path('favorites/', views.user_favorites, name='favorites'),
    path('add_to_favorites/<int:ad_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('ad/delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
