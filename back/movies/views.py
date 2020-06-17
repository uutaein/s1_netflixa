from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie
from .serializers import MovieListSerializer, MovieSerializer, MovieCreateSerializer
from accounts.serializers import UserSerializer

import operator

@api_view(['GET'])
def list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@user_passes_test(lambda u: u.is_superuser)
def create(request):
    serializer = MovieCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@user_passes_test(lambda u: u.is_superuser)
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCreateSerializer(data=request.data, instance=movie)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
@user_passes_test(lambda u: u.is_superuser)
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return Response({'message': 'movie deleted'})

@api_view(['GET'])
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 좋아요를 누른적이 있다면, => DB에 저장되어 있으면
    if movie.like_users.filter(id=request.user.pk).exists():
        movie.like_users.remove(request.user)
        return Response({'message': 'movie unliked'})
    else:
        movie.like_users.add(request.user)
        return Response({'message': 'movie liked'})

# ----------------------------------------------------- #
from itertools import chain
@api_view(['GET'])
def recommend(request):
    favorite_genres = []
    genre_cnt = {}
    User = get_user_model()
    user = get_object_or_404(User, pk=request.user.pk)
    serializer = UserSerializer(user)
    for movie_id in serializer.data['like_movies']:
        movie = get_object_or_404(Movie, pk=movie_id)
        movie_serializer = MovieSerializer(movie)
        favorite_genres.extend(movie_serializer.data['genres'])
    fav_gen_set = set(favorite_genres)
    for genre_id in fav_gen_set:
        genre_cnt[genre_id] = favorite_genres.count(genre_id)

    sorted_dict = sorted(genre_cnt.items(), key=operator.itemgetter(1), reverse=True)

    favorite1 = int(sorted_dict[0][1])
    favorite2 = int(sorted_dict[1][1])
    favorite3 = int(sorted_dict[2][1])
    favorites_sum = favorite1+favorite2+favorite3
    first = int((favorite1/favorites_sum)*20)
    second = int((favorite2/favorites_sum)*20)
    third = int((favorite3/favorites_sum)*20)

    movies1 = Movie.objects.filter(genres=sorted_dict[0][0]).order_by('-vote_average')[:20]
    movies2 = Movie.objects.filter(genres=sorted_dict[1][0]).order_by('-vote_average')
    movies3 = Movie.objects.filter(genres=sorted_dict[2][0]).order_by('-vote_average')

    favorites_serializer1 = MovieListSerializer(movies1, many=True)
    favorites_serializer2 = MovieListSerializer(movies2, many=True)
    favorites_serializer3 = MovieListSerializer(movies3, many=True)

    return Response(favorites_serializer1.data)
