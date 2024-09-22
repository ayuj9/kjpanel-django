#!/bin/bash

echo "setting enviornment"

python3 -m venv .django_env
source .django_env/bin/activate

echo "virtual env created and activated"
which python3

echo "installing dependencies"
pip install -r requirements.txt

echo "migrating"
python manage.py migrate

echo "starting server"
python manage.py runserver



