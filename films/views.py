from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from .models import FilmsCategory, Films
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from users.forms import CommentFormFilm, RatingFilmForm
from users.models import RatingFilms
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
# Create your views here.

class FilmsListView(ListView):

    model = Films
    template_name = 'films.html'


    def get_queryset(self):
        queryset = super(FilmsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FilmsListView, self).get_context_data()
        context['categories'] = FilmsCategory.objects.all()
        return context


class OneFilmView(FormMixin, DetailView):

    model = Films
    template_name = 'one-film.html'
    form_class = CommentFormFilm
    success_msg = 'Комментарий успешно добавлен'

    def get_success_url(self, **kwargs):
        return reverse_lazy('filmspage:one_film', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.film = self.get_object()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        film = Films.objects.get(id=self.kwargs.get('pk'))
        context['rating_form'] = RatingFilmForm()
        if RatingFilms.objects.filter(film=film):
            context['OneRatingFilm'] = RatingFilms.objects.get(Q(user=user) and Q(film=film))
            return context
        else:
            return context


class AddFilmsRating(CreateView):
    model = RatingFilms
    form_class = RatingFilmForm
    template_name = 'rating-film.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('filmspage:films')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.form_invalid(form)

    def form_valid(self, form, **kwargs):

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.film = Films.objects.get(id=self.kwargs.get('pk'))
        self.object.save()
        return super().form_valid(form)


def create_rating(request, **kwargs):
    cinema_id = kwargs.get('pk')
    if request.method == 'POST':
        cinema = get_object_or_404(Films, id=cinema_id)
        user = request.user
        rating = request.POST.get('rating')
        rating_obj = RatingFilms.objects.filter(user=user, film=cinema)
        if rating_obj:
            rating_obj.update(rating=rating)
        else:
            rating = RatingFilms(user=user, film=cinema, rating=rating)
            rating.save()
        return redirect('filmspage:one_film', pk=cinema_id)

# class FilmAddRating(CreateView):
#     model = RatingFilms
#     form_class = RatingFilmForm
#     template_name = 'rating-film.html'
#     success_url = 'filmspage:films'
#
#     # def get_success_url(self, **kwargs):
#     #     return reverse_lazy('animepage:anime', kwargs={'pk': self.get_object().id})
#
#     def post(self, request, *args, **kwargs):
#         user = self.request.user
#         film = Films.objects.get(id=self.kwargs.get('pk'))
#         form = self.get_form()
#         if form.is_valid():
#             RatingFilms.objects.update_or_create(
#                 user=user,
#                 film=film,
#                 # rating=int(request.POST.get('rating')),
#                 defaults={'rating': int(request.POST.get('rating'))}
#             )
#             return HttpResponseRedirect('/films')
#             # return self.form_valid(form)
#         else:
#             self.form_invalid(form)