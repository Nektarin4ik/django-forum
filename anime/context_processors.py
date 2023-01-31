from users.models import RatingAnime
from.models import Anime
from django.db.models import Q
#
#
# def ratingAnime(request, **kwargs):
#     print('1')
#     user = request.user
#     print('2')
#     a = {'pk': kwargs}
#     b = a.values()
#     if b:
#         print('3')
#         anime = Anime.objects.get(id=kwargs.get('pk'))
#
#         if anime is int:
#             print('5')
#             print('6')
#             return {
#                 'ratingAnime': RatingAnime.objects.filter(Q(user=user) and Q(anime=anime)) if user.is_authenticated else []}
#
#         elif anime:
#             print(anime)
#             return {
#                 'ratingAnime': RatingAnime.objects.filter(user=user) if user.is_authenticated else []}
#         else:
#             return None
#
def ratingAnime(request):
    user = request.user
    return {'ratingAnime': RatingAnime.objects.filter(user=user) if user.is_authenticated else []}