from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from .models import Movie, Rank
from .serializers import MovieListSerializers, MovieSerializers, RankListSerializers, RankSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    # movies = get_list_or_404(Movie.objects.order_by(''))
    # https://wayhome25.github.io/django/2017/03/01/django-99-my-first-project-5/ 참조
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializers(movies, many=True)
    return Response(serializers.data)
    # return R

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
     movie = get_object_or_404(Movie, pk=movie_pk)
     serializer = MovieSerializers(movie)
     return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def rank_list_create(request, movie_pk):

    if request.method == 'GET':
        ranks = get_list_or_404(Rank, movie_id=movie_pk)
        serializers = RankListSerializers(ranks, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = RankSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def rank_delete(request, movie_pk, rank_pk):
    rank = get_object_or_404(Rank, pk=rank_pk)
    rank.delete()
    return Response({ 'id':rank_pk }, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def rank_likes(request, movie_pk, rank_pk):
    user = request.user
    rank = get_object_or_404(Rank, pk=rank_pk)

    if request.method == 'GET':
        if user in rank.like_users.all():
            liked = True
        else:
            liked = False
        context = {
            'liked': liked,
            'count': rank.like_users.count()
        }
        return Response(context)
    elif request.method == 'POST':
        if user in rank.like_users.all():
            rank.like_users.remove(user)
            liked = False
        else:
            rank.like_users.add(user)
            liked = True
        context = {
            'liked': liked,
            'count': rank.like_users.count()
        }
        return Response(context)