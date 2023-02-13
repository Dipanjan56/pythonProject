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
make migration for installed apps in settings.py with project level:
terminal ->  python3 manage.py migrate

Step 6
add go to apps.py in app level and copy th class_name : e.g ThirdAppConfig
then add like this 'third_app.apps.ThirdAppConfig' in installed_apps in project level settings.py

Step 6
terminal -> python3 manage.py makemigrations third_app


"""
