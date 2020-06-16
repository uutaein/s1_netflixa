from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'popularity', 'vote_average', 'release_date')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id',)

class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['like_users', 'popularity', 'vote_count', 'vote_average']