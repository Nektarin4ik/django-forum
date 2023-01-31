from django.contrib import admin
from django.urls import path
from .views import AnimeListView, OneAnimeView, AnimeAddRating, create_rating
# from static.views import anime_detail, create_comment ТЕСТ ЧАТ ГПТ


app_name = 'animepage'

urlpatterns = [
    path('', AnimeListView.as_view(), name='anime'),
    path('category/<int:category_id>', AnimeListView.as_view(), name='filter_anime'),
    path('<int:pk>/', OneAnimeView.as_view(), name='one_anime'),
    # path('<int:anime_id>/', anime_detail, name='one_anime'), ТЕСТ ЧАТ ГПТ
    # path('<int:anime_id>/comment', create_comment, name='create_comment'), ТЕСТ ЧАТ ГПТ
    path('<int:pk>/rating', create_rating, name='create_rating'),
    # path('add_rating/<int:pk>', AnimeAddRating.as_view(), name='rating'), ТЕСТ ЧАТ ГПТ
]