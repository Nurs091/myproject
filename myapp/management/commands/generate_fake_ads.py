import random
from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import Ad, User, Category, AdStatus

fake = Faker()

class Command(BaseCommand):
    help = "Генерирует случайные объявления"

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        categories = list(Category.objects.all())
        statuses = list(AdStatus.objects.all())

        if not users or not categories or not statuses:
            self.stdout.write(self.style.ERROR("Нет пользователей, категорий или статусов!"))
            return

        for _ in range(20):  # Сколько объявлений создать
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

        self.stdout.write(self.style.SUCCESS("Случайные объявления созданы."))
