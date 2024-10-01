# my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),  # Root path to render the register.html
]
