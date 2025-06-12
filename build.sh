#!/usr/bin/env bash

# Создание и применение миграций
python manage.py makemigrations
python manage.py migrate

# Сборка статических файлов (если нужно)
python manage.py collectstatic --noinput