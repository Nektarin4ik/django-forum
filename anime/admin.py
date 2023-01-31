from django.contrib import admin
from .models import AnimeCategory, Anime
# Register your models here.

@admin.register(AnimeCategory)
class AnimeCategory(admin.ModelAdmin):
    list_display = ['name', 'description']
    ordering = ['name']
    list_per_page = 10

@admin.register(Anime)
class Anime(admin.ModelAdmin):
    list_display = ['anime', 'rating', 'studio', 'description']
    ordering = ['rating']
    list_per_page = 10