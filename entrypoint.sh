#!/bin/bash

echo "DATABASE_NAME - $DATABASE_NAME"
echo "DATABASE_USER - $DATABASE_USER"
echo "DATABASE_PASSWORD - $DATABASE_PASSWORD"
echo "DATABASE_HOST - $DATABASE_HOST"
echo "DATABASE_PORT - $DATABASE_PORT"

python manage.py migrate

python manage.py runserver