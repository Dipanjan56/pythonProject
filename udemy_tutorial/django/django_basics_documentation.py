""" Django is web development framework
Key Features of django:
1. Model-Template-View Structure (MTV)
2. ORM - Object-relational Mapper
3. Models
4. URLs and views
5. Templates

web struture:

|----------------CLIENT SIDE--------------------------|---------------------------------------------SERVER SIDE-----------------------------------------------------------------------------|
|----------------TEMPLATE-----------------------------|--------------------------------VIEW---------------------------------------|-------------------------MODEL---------------------------|

[user browser] <-> [html,css,js using jinja framework] <-[python file using django framework] <-> [python file with URL Routing] <-> [Models - python file using django models] <-> Database

Step 1
Installation:
1. terminal -> python -m pip install Django
2. check version: -> python3 -c "import django; print(django.get_version())"

Step 2
Start new Project:
3. terminal -> django-admin startproject my_site

Step 3
Start new App:
terminal -> cd /my_site-> python3 manage.py startapp my_app

Step 4
Run App:
terminal ->  python3 manage.py runserver

Step 5
Database creation and integration:
it will create migration instruction in project level
terminal ->  python3 manage.py makemigrations third_app

Step 6:
it will carry out the instruction and will create db.sqllite3 in your project and
make migration for installed apps/ tables in DB in settings.py with project level:
terminal -> python3 manage.py migrate

Step 7
add go to apps.py in app level and copy th class_name : e.g ThirdAppConfig
then add like this 'third_app.apps.ThirdAppConfig' in installed_apps in project level settings.py



Note:
    Migration: In general, migration is the act of connecting changes in your Django project or app to the database
               This includes things like adding models within app, ading new app, updating models
               with a new column/attribute and more

               we typically manage these command in manage.py file once you create model ->
               1. makemigrations: it sets the instruction to perform the update/create activity,
                                  but does not create on its own
               2. migrate: we need to then run this command to perform the activity
               3. sqlmigrate : if u wanted to see what sql code look like, the run this command

    Command DB: Patient.object.get(pk=1) -> here pk means Primary Key and
                always starts from 1 not 0 like array positioning


Step 8:
create superuser [admin]:
terminal -> python3 manage.py createsuperuser
username: admin
email: dipanjan56@gmail.com
password: Test@123

"""
