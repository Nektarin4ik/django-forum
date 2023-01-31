from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from anime.models import Anime
from films.models import Films


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_emails = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'


class CommentsAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Комментируемое аниме',
                              blank=True, null=True, related_name='CommentsAnime_Anime')
    create_date = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=400)


    def __str__(self):
        return f'{self.comment}'


class CommentsFilm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    film = models.ForeignKey(Films, on_delete=models.CASCADE, verbose_name='Комментируемый фильм',
                              blank=True, null=True, related_name='CommentsFilm_Films')
    create_date = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=400)


    def __str__(self):
        return f'{self.comment}'


class RatingAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор рейтинга', blank=True, null=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Оцениваемое аниме',
                              blank=True, null=True, related_name='RatingAnime_Anime')
    create_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True, null=True)

    def __str__(self):
        return f'{self.rating}'

    class Meta:
        ordering = ['-rating']
# class RatingStarAnime(models.Model):
#     value = models.SmallIntegerField('Значение', default=0)
#     def __str__(self):
#         return f'{self.value}'
#     class Meta:
#         verbose_name = 'Звезды рейтинга'
#         verbose_name_plural = 'Звезды рейтинга'
#         ordering = ['-value']

class RatingFilms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    film = models.ForeignKey(Films, on_delete=models.CASCADE, verbose_name='Комментируемый фильм',
                              blank=True, null=True, related_name='RatingFilms_Films')
    create_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True, null=True)

    def __str__(self):
        return f'{self.rating}'

    class Meta:
        ordering = ['-rating']
