#!/usr/bin/env bash

pip install -r requirements.txt

# Создание и применение миграций
python manage.py makemigrations
python manage.py migrate

# Сборка статических файлов (если нужно)
python manage.py collectstatic --noinput
