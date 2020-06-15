from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# from .models import User
from .serializers import UserSerializer

User = get_user_model()

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


# @api_view(['GET'])
# def delete(request):
#     request.user.delete()
#     return Response({'message':'delete success'})

@api_view(['GET'])
def follow(request, user_pk):
    # 팔로우 당하는 사람
    user = get_object_or_404(User, pk=user_pk)
    if user != request.user:
        # 팔로우를 요청한 사람 => request.user
        # 팔로우가 되어 있다면,
        if user.fans.filter(pk=request.user.pk).exists():
            # 삭제
            user.fans.remove(request.user)
            return Response({'message': 'unfollow'})
        else:
            # 추가
            user.fans.add(request.user)
            return Response({'message': 'follow'})
    return Response({'message': '본인입니다.'})



# @api_view(['POST'])
# def update(request, user_pk):
#     user = get_object_or_404(User, pk=user_pk)
#     serializer = UserSerializer(data=request.data, instance=user)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)




