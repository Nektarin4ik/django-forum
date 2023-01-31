from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Anime, AnimeCategory
from django.views.generic.edit import FormMixin
from users.forms import CommentFormAnime, RatingAnimeForm
from users.models import RatingAnime, CommentsAnime
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


class AnimeListView(ListView):

    model = Anime
    template_name = 'anime.html'

    def get_queryset(self):
        queryset = super(AnimeListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        # if category_id == None:
        #     category_id = 3
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnimeListView, self).get_context_data()
        context['categories'] = AnimeCategory.objects.all()
        return context


class OneAnimeView(FormMixin, DetailView):

    model = Anime
    template_name = 'one-anime.html'
    form_class = CommentFormAnime
    success_msg = 'Комментарий успешно добавлен'

    def get_success_url(self, **kwargs):
        return reverse_lazy('animepage:one_anime', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.anime = self.get_object()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        anime = Anime.objects.get(id=self.kwargs.get('pk'))
        context['rating_form'] = RatingAnimeForm()
        if RatingAnime.objects.filter(anime=anime):
            context['OneRatingAnime'] = RatingAnime.objects.get(Q(user=user) and Q(anime=anime))
            return context
        else:
            return context
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['RatForm'] = RatingAnime()
    #     return context


def create_rating(request, **kwargs):
    anime_id = kwargs.get('pk')
    if request.method == 'POST':
        anime = get_object_or_404(Anime, id=anime_id)
        user = request.user
        rating = request.POST.get('rating')
        rating_obj = RatingAnime.objects.filter(user=user, anime=anime)
        if rating_obj:
            rating_obj.update(rating=rating)
        else:
            rating = RatingAnime(anime=anime, user=user, rating=rating)
            rating.save()
        return redirect('animepage:one_anime', pk=anime_id)


class AnimeAddRating(CreateView):
    model = RatingAnime
    form_class = RatingAnimeForm
    template_name = 'rating-anime.html'
    success_url = 'animepage:anime'

    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('animepage:anime', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        # form = RatingAnimeForm(request.POST)
        user = self.request.user
        anime = Anime.objects.get(id=self.kwargs.get('pk'))
        form = self.get_form()
        if form.is_valid():
            RatingAnime.objects.update_or_create(
                user=user,
                anime=anime,
                # rating=int(request.POST.get('rating')),
                defaults={'rating': int(request.POST.get('rating'))}
            )
            print('5')
            return HttpResponseRedirect('/anime')
            # return self.form_valid(form)
        else:
            self.form_invalid(form)





    # def form_valid(self, form, **kwargs):
    #
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.anime = Anime.objects.get(id=self.kwargs.get('pk'))
    #     self.object.save()
    #     return super().form_valid(form)



# class AddRating(View):
#
#     def get_user(self, request):
#         x_forward = request.META.get('user.id')
#         if x_forward:
#             iduser = int(x_forward)
#         else:
#             None
#         return iduser
#
#     def post(self, request):
#         form = RatingAnime(request.POST)
#         if form.is_valid():
#             RatingAnime.objects.update_or_create(
#                 anime=int(request.POST.get('anime.id')),
#                 user=self.get_user(request),
#                 # user=int(request.POST.get('user.id')),
#                 defaults={'rating_id': int(request.POST.get('rating'))}
#             )



    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.anime = self.request.anime
    #     self.object.save()
    #     return reverse_lazy('animepage:anime')


    # 1) Наследование классов, с помощью прошлого класса попробовать отобразить 2 формы
    # 2) Расширение шаблонов, отдельный шаблон в котором рейтинг
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(OneListView, self).get_context_data()
    #     anime_id = self.kwargs.get('anime_id')
    #     context['anime'] = AnimeCategory.objects.get(anime_id)
    #     return context

    # def get_queryset(self):
    #     queryset = super(OneListView, self).get_queryset()
    #     anime_id = self.kwargs.get('anime_id')
    #     return queryset.filter(anime_id=anime_id)


# class CommentOneAnime(View):
#
#     def get(self, request, **kwargs):
#         anime_id = self.kwargs.get('anime_id')
#         context = {
#             'anime': Anime.objects.get(id=anime_id)
#         }
#         return render(request, 'one-film.html', context)
#
#     def post(self, request):
#
#         form = CommentsAnime()
