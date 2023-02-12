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


Installation:
1. terminal -> python -m pip install Django
2. check version: -> python3 -c "import django; print(django.get_version())"

Start new Project:
3. terminal -> django-admin startproject my_site


Start new App:
terminal -> cd /my_site-> cd  python3 manage.py startapp my_app

Run App:
terminal ->  python3 manage.py runserver


"""