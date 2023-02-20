from django.http import *
from django.shortcuts import render


# Create your views here.
def simple_view(request):
    return render(request, 'second_app/example.html')  # .html
