@echo off
echo Running migrations on main...
python manage.py makemigrations main
python manage.py migrate main

echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo Starting Django development server...
python manage.py runserver
