from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes

from .models import Movie
from .serializers import MovieListSerializer


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
