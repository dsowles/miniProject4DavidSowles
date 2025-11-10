# INF601 - Advanced Programming in Python
# Name: David A. Sowles
# Project: Mini Project 4
# Date of Creation 11/07/2025

from django.shortcuts import render,get_object_or_404
from .models import Animal

# Create your views here.
def animal_list(request):
    # Get all animal records.
    animals = Animal.objects.all()
    return render(request, "blog/animal_list.html", {"animals": animals})

def animal_detail(request, pk):
    # Get the particular animal record, or redirect to 404 page.
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, "blog/animal_detail.html", {"animal": animal})