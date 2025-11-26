# p32_django

# створюємо і активуємо venv (приклад для Unix / macOS)
python3.14 -m venv venv
source venv/bin/activate

# для Windows (PowerShell)
# python -m venv venv
# venv\Scripts\activate

pip install django  

django-admin startproject mysite .

python manage.py runserver