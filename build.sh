#!/usr/bin/env bash

# Установка зависимостей
pip install -r requirements.txt

# Применение миграций
python manage.py makemigrations
python manage.py migrate

# Загрузка фикстур (важно делать ПОСЛЕ миграций)
python manage.py loaddata categories.json  # Сначала категории
python manage.py loaddata ads.json        # Затем объявления

# Сборка статических файлов
python manage.py collectstatic --noinput