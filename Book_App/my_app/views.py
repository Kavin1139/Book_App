# my_app/views.py
from django.shortcuts import render

def register(request):
    return render(request, 'register.html')
