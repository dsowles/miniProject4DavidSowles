# INF601 - Advanced Programming in Python
# Name: David A. Sowles
# Project: Mini Project 4
# Date of Creation 11/07/2025

from django.db import models

# Create your models here.

# Animal class for use in blog app.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name