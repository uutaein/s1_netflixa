from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Movie
        fields = ('title')

# class ReviewSerializer(serialziers.ModelSerializer):
#     user = UserSerializer(required=False)
    
#     class Meta:
#         model = Review
#         fields = '__all__'
#         read_only_fields = ('id', 'user', 'created_at', 'updated_at')