# Common Criteria Global Certification Status

### Project Preview
<img src="https://github.com/hongbo-wei/CC-Global-Status/blob/main/Project%20Preview.png?raw=true">

Django Commands in Terminal:

    // Make a new project
    django-admin startproject myproject 

    // Make a new app
    python manage.py startapp myapp

    // Run the app
    python manage.py runserver

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
