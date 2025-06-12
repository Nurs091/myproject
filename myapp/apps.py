from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.translation


# myapp/apps.py
from django.db.utils import OperationalError

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        from myapp.models import Category
        try:
            categories = [
                "Business",
                "Kids&Babies",
                "Hobbies&Sports",
                "Animals",
                "Services",
                "Jobs",
                "Clothing&Accessories",
                "Home&Garden",
                "Electronics",
                "Vehicles",
                "Apartment",
            ]
            for name in categories:
                Category.objects.get_or_create(name=name)
        except OperationalError:
            # База еще не готова (при миграциях), просто пропускаем
            pass
