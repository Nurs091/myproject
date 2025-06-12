from django.core.management.base import BaseCommand
from faker import Faker
import random
from myapp.models import Category, Ad, User, AdStatus

fake = Faker()

class Command(BaseCommand):
    help = "Генерирует случайные объявления (без создания категорий)"

    def handle(self, *args, **kwargs):
        # Получаем все категории, пользователей и статусы
        categories = list(Category.objects.all())
        users = list(User.objects.all())
        statuses = list(AdStatus.objects.all())

        if not categories:
            self.stdout.write(self.style.ERROR("Нет доступных категорий."))
            return

        if not users or not statuses:
            self.stdout.write(self.style.ERROR("Не хватает пользователей или статусов для создания объявлений."))
            return

        # Генерация объявлений
        for _ in range(20):
            Ad.objects.create(
                title=fake.sentence(),
                description=fake.text(),
                price=round(random.uniform(10, 1000), 2),
                author=random.choice(users),
                category=random.choice(categories),
                status=random.choice(statuses),
                city=fake.city(),
                language=random.choice(['ru', 'en'])
            )

        self.stdout.write(self.style.SUCCESS("Созданы случайные объявления."))
