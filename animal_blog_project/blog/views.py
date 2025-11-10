# INF601 - Advanced Programming in Python
# Name: David A. Sowles
# Project: Mini Project 4
# Date of Creation 11/07/2025

from django.shortcuts import render,get_object_or_404,redirect
from .models import Animal
from .forms import AnimalForm

# Create your views here.
def animal_list(request):
    # Get featured animal records.
    featured_animals = Animal.objects.filter(featured=True)
    # Get animal records which are not featured.
    animals = Animal.objects.filter(featured=False)
    return render(request, "blog/animal_list.html", {
        "featured_animals": featured_animals,
        "animals": animals,
    })

def animal_detail(request, pk):
    # Get the particular animal record, or redirect to 404 page.
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, "blog/animal_detail.html", {"animal": animal})

# View to handle adding a new animal entry to the blog.
def add_animal(request):
    if request.method == "POST":
        # Bind the submitted data.
        form = AnimalForm(request.POST, request.FILES)
        # Validate form data
        if form.is_valid():
            # Save to the database
            form.save()
            # Redirect back to the list after saving to the database.
            return redirect("blog:animal_list")
    else:
        # If the request was not a POST, create an empty form for the user.
        form = AnimalForm()
    return render(request, "blog/add_animal.html", {"form": form})