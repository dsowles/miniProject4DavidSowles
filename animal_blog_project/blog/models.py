# INF601 - Advanced Programming in Python
# Name: David A. Sowles
# Project: Mini Project 4
# Date of Creation 11/07/2025

from django.db import models

# Create your models here.

# Animal class for use in blog app.
class Animal(models.Model):
    # The animal's display name
    name = models.CharField(max_length=100)
    # The species
    species = models.CharField(max_length=100)
    # A description of the animal, which can be a much longer text.
    description = models.TextField()
    # Optional image for the animal.
    image = models.ImageField(upload_to="animal_images/", blank=True, null=True)
    # Date which the entry was created.
    date_added = models.DateTimeField(auto_now_add=True)

    # Meta class for ordering entries. Newest first.
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name