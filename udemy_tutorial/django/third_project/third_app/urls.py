from django.urls import path
from . import views

# register in app namespace
# URL NAMES
app_name = 'third_app'
urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
    path('inherited/', views.inherited_view, name='inherited')
]
