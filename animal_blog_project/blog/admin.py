# INF601 - Advanced Programming in Python
# Name: David A. Sowles
# Project: Mini Project 4
# Date of Creation 11/07/2025

from django.contrib import admin

# Blog app model imports
from .models import Animal

# Update admin site's blog settings.
admin.site.site_header = "🐾 Animal Blog Admin"
admin.site.site_title = "Animal Blog"
admin.site.index_title = "Welcome to the Animal Blog Admin"

# Register your models here.

# This decorator tells Django to use the following class def to register the animal model
# with the Django admin site.
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    # Column names for admin table.
    list_display = ('name', 'species', 'date_added')
    # The following will be used by Django to setup a search bar.
    search_fields = ('name', 'species')
    # Adds a sidebar fileter.
    list_filter = ('species',)