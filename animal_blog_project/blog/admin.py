# INF601 - Advanced Programming in Python
# Name: David A. Sowles
# Project: Mini Project 4
# Date of Creation 11/07/2025

from django.contrib import admin
# Blog app model imports
from .models import Animal
from django.utils.html import format_html

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
    list_display = ('name', 'species', 'date_added', 'thumbnail','featured')
    # The following will be used by Django to setup a search bar.
    search_fields = ('name', 'species')
    # Adds a sidebar fileter.
    list_filter = ('species',)

    list_editable = ('featured',)
    ordering = ('-featured', '-date_added')

    fieldsets = (
        ('Animal Info', {
            'fields': ('name', 'species', 'description')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Metadata', {
            'fields': ('featured', 'date_added'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('date_added',)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;">', obj.image.url)
        return "—"
    thumbnail.short_description = "Image"

    class Media:
        css = {
        'all': ('admin/css/custom_admin.css',)
    }