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

python manage.py migrate

python manage.py createsuperuser
# ім'я користувача, email (можна пропустити), пароль

python manage.py startapp blog

python manage.py makemigrations
python manage.py migrate

python manage.py shell

from blog.models import Post




post = Post.objects.create(
    title="Мій перший пост",
    content="Текст першого поста",
    is_published=True,
)
post.save()

post = Post(
    title="Чернетка",
    content="Це чернетка",
)
post.save()




posts = Post.objects.all()
posts
<QuerySet [<Post: Мій перший пост>, <Post: Чернетка>]>