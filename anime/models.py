from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class AnimeCategory(models.Model):

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Anime Categories'

    def __str__(self):
        return self.name



class Anime(models.Model):

    anime = models.CharField(max_length=30)
    studio = models.CharField(max_length=30)
    rating = models.PositiveIntegerField(blank=True, validators=[MaxValueValidator(100)])
    image = models.ImageField(upload_to='anime_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    category = models.ForeignKey(AnimeCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.anime}'

