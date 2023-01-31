from django.contrib import admin
from .models import FilmsCategory, Films
# Register your models here.

@admin.register(FilmsCategory)
class FilmsCategory(admin.ModelAdmin):
    list_display = ['name', 'description']
    ordering = ['name']
    list_per_page = 10

@admin.register(Films)
class Films(admin.ModelAdmin):
    list_display = ['cinema', 'rating', 'producer', 'description']
    ordering = ['rating']
    list_per_page = 10