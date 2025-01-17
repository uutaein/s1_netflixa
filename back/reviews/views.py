from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Review, Comment
from movies.models import Movie
from .serializers import ReviewSerializer, ReviewListSerializer, CommentSerializer

@api_view(['GET'])
def index(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


# Review CRUD
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['POST'])
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        return Response({'message': '본인의 글만 수정할 수 있습니다.'})

@api_view(['GET'])
def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
        return Response({'message': 'review deleted'})
    else:
        return Response({'message': '본인의 글만 삭제할 수 있습니다.'})

# review like
@api_view(['GET'])
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # 좋아요를 누른적이 있다면, => DB에 저장되어 있으면
    if review.like_users.filter(id=request.user.pk).exists():
        review.like_users.remove(request.user)
        return Response({'message': 'review unliked'})
    else:
        review.like_users.add(request.user)
        return Response({'message': 'review liked'})


# comment CRUD
@api_view(['GET'])
def comments_list(request, review_pk):
    comments = Comment.objects.filter(review_id=review_pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, review_pk):
    serializer = CommentSerializer(data=request.data)
    review = get_object_or_404(Review, pk=review_pk)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data)

@api_view(['POST'])
def update_comment(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(data=request.data, instance=comment)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def delete_comment(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return Response({'message': 'comment deleted'})
    else:
        return Response({'message': '본인의 글만 삭제할 수 있습니다.'})


#  score C,U,D