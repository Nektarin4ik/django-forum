from django.contrib import admin
from django.urls import path
from .views import FilmsListView, OneFilmView, AddFilmsRating, create_rating

app_name = 'filmspage'

urlpatterns = [
    path('', FilmsListView.as_view(), name='films'),
    path('category/<int:category_id>', FilmsListView.as_view(), name='film_filter'),
    path('<int:pk>', OneFilmView.as_view(), name='one_film'),
    path('<int:pk>/rating', create_rating, name='create_rating'),
    # path('add_rating/<int:pk>', AddFilmsRating.as_view(), name='rating'),

]