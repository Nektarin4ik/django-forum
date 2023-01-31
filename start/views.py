from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views import View
from anime.models import Anime
from films.models import Films
from users.models import RatingAnime, RatingFilms
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class TopsWeek(View):

    def get(self, request):

        a = RatingAnime.objects.filter(rating__gt=80)
        b = RatingFilms.objects.filter(rating__gt=80)
        context = {
            'Films': b,
            'Anime': a,
        }
        return render(request, 'tops-week.html', context)




