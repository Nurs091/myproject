#!/usr/bin/env bash

# Установка зависимостей
pip install -r requirements.txt

# Применение миграций
python manage.py makemigrations
python manage.py migrate

# Загрузка фикстур
python manage.py loaddata categories.json
python manage.py loaddata statuses.json  # если у тебя есть статусы

# Генерация случайных объявлений
python manage.py generate_fake_ads

# Сборка статики
python manage.py collectstatic --noinput
