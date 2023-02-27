#!/bin/bash

cd /app/
/opt/venv/bin/python manage.py migrate --noinput || true
/opt/venv/bin/python manage.py createsuperuser --email $DJANGO_SUPERUSER_EMAIL --noinput || true