from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Review, Comment, Score

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Review
        fields = ('id', 'title', 'user', 'like_users')

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        exclude =['like_users']
        read_only_fields = ('id', 'user', 'movie', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'created_at')