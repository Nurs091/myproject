from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_ads, name='category_ads'),
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('create/', views.create_ad, name='create_ad'),
    path('ad/<int:ad_id>/edit/', views.edit_ad, name='edit_ad'),
    path('ad/delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),

    path('profile/', views.user_profile, name='profile'),

    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
