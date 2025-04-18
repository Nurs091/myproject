from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('register/', views.register, name='register'),  # Страница регистрации
    path('login/', views.user_login, name='login'),  # Страница входа
    path('logout/', views.user_logout, name='logout'),  # Страница выхода
    path('create-ad/', views.create_ad, name='create_ad'),  # Страница создания объявления
]

# Добавляем обработку медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
