from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class FilmsCategory(models.Model):

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Films Categories'

    def __str__(self):
        return self.name


class Films(models.Model):

    cinema = models.CharField(max_length=30)
    producer = models.CharField(max_length=30)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(100)])
    image = models.ImageField(upload_to='films_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    category = models.ForeignKey(FilmsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cinema}'

    class Meta:
        ordering = ['-rating']