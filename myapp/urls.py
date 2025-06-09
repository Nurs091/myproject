from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    ResetPasswordView, ForgotPasswordView, VerifyResetCodeView,
    AdViewSet, AdStatusViewSet, CategoryViewSet, UserViewSet,
    RegisterAPIView, VerifyEmailAPIView
)

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'statuses', AdStatusViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    # Пути без языкового префикса (API, смена языка)
    path('api/', include(router.urls)),
    path('api/register/', RegisterAPIView.as_view(), name='api-register'),
    path('api/verify-email/', VerifyEmailAPIView.as_view(), name='api-verify-email'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('verify-reset-code/', VerifyResetCodeView.as_view(), name='verify_reset_code'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),

    # Остальные пути с языковым префиксом — просто пути без i18n_patterns здесь!
    path('register/', views.register_page, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_ads, name='category_ads'),
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('create/', views.create_ad, name='create_ad'),
    path('profile/', views.user_profile, name='profile'),
    path('favorites/', views.user_favorites, name='favorites'),
    path('add_to_favorites/<int:ad_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('ad/delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('ad/<int:ad_id>/update-status/', views.update_ad_status, name='update_ad_status'),
    path('ad/<int:ad_id>/edit/', views.edit_ad, name='edit_ad'),
    path('moderation/', views.moderation_panel, name='moderation_panel'),
    path('moderation/approve/<int:ad_id>/', views.approve_ad, name='approve_ad'),
    path('moderation/reject/<int:ad_id>/', views.reject_ad, name='reject_ad'),
    path('moderation/ad/<int:ad_id>/', views.moderation_ad_detail, name='moderation_ad_detail'),
    path('verify-code/', TemplateView.as_view(template_name='verify_code.html'), name='verify-code'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)