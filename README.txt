In Terminal:

1. $ django-admin startproject myproject
2. $ python manage.py startapp myapp
3. $ python manage.py runserver

Check model columns' inforamtion:
    python manage.py inspectdb mytable

Change your models (in models.py).
     > python3 manage.py migrate
    The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to
    the database settings in my_project/settings.py file and the database migrations shipped with the app.

    > python3 manage.py makemigrations
    By running makemigrations, you’re telling Django that you’ve made some changes to your models
    and that you’d like the changes to be stored as a migration.
    Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk.