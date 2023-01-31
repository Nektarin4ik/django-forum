# from django.shortcuts import render, get_object_or_404
# from .models import Comment, Rating
#
# def movie_detail(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     comments = Comment.objects.filter(movie=movie)
#     ratings = Rating.objects.filter(movie=movie)
#     context = {'movie': movie, 'comments': comments, 'ratings': ratings}
#     return render(request, 'movie_detail.html', context)
#
# def create_comment(request, movie_id):
#     if request.method == 'POST':
#         movie = get_object_or_404(Movie, id=movie_id)
#         user = request.user
#         text = request.POST.get('text')
#         comment = Comment(movie=movie, user=user, text=text)
#         comment.save()
#         return redirect('movie_detail', movie_id=movie_id)
#
# def create_rating(request, movie_id):
#     if request.method == 'POST':
#         movie = get_object_or_404(Movie, id=movie_id)
#         user = request.user
#         rating = request.POST.get('rating')
#         rating_obj = Rating.objects.filter(user=user, movie=movie)
#         if rating_obj:
#             rating_obj.update(rating=rating)
#         else:
#             rating = Rating(movie=movie, user=user, rating=rating)
#             rating.save()
#         return redirect('movie_detail', movie_id=movie_id)
#
# from django.db import models
#
# class Comment(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
# class Rating(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.PositiveSmallIntegerField()
#
#
# {% extends 'base.html' %}
#
# {% block content %}
#   <h1>{{ movie.title }}</h1>
#   <h2>Comments</h2>
#   <ul>
#     {% for comment in comments %}
#       <li>{{ comment.text }} (posted by {{ comment.user.username }})</li>
#     {% endfor %}
#   </ul>
#   <h2>Ratings</h2>
#   <ul>
#     {% for rating in ratings %}
#       <li>{{
#
#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
#     path('movie/<int:movie_id>/create_comment/', views.create_comment, name='create_comment'),
#     path('movie/<int:movie_id>/create_rating/', views.create_rating, name='create_rating'),
# ]
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('text',)
#
# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields = ('rating',)