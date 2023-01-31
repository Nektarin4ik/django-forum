from django.contrib import admin
from django.urls import path, include
from start.views import IndexView, TopsWeek
from films.views import FilmsListView
from anime.views import AnimeListView
app_name = 'basepage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('tops', TopsWeek.as_view(), name='top_week'),
                ]
