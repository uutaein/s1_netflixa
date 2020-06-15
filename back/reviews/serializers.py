from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Review, Comment

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Review
        fields = ('id', 'title', 'user',)

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = ('id', 'content',)
