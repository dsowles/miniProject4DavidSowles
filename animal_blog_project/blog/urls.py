# INF601 - Advanced Programming in Python
# Name: David A. Sowles
# Project: Mini Project 4
# Date of Creation 11/07/2025

from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.animal_list, name="animal_list"),
    path("<int:pk>/", views.animal_detail, name="animal_detail"),
    path("add/", views.add_animal, name="add_animal"),
]