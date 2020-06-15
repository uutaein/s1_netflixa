from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie
from .serializers import MovieListSerializer, MovieSerializer


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
def create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(data=request.data, instance=movie)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
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
