from django.urls import path

from . import views

app_name = 'cars'
urlpatterns = [
    path('list/', views.list, name='list_car'),
    path('add/', views.add, name='add_car'),
    path('delete/', views.delete, name='delete_car'),
]
