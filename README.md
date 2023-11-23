# Common Criteria Global Certification Status

## Project Preview

<img src="https://github.com/hongbo-wei/CC-Global-Status/blob/main/Project%20Preview.png?raw=true">

### Instructions

Django Commands in Terminal:

    # Run the app
    python manage.py runserver

Check database model inforamtion:

    # You can add your table name or not
    python manage.py inspectdb (mytable)

By running makemigrations, you’re telling Django that you’ve made some changes to your models and that you’d like the changes to be stored as a migration. Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk.

    python3 manage.py makemigrations

Migrate your models (in models.py):

     python3 manage.py migrate

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in my_project/settings.py file and the database migrations shipped with the app.
