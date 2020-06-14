from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # moives
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
]

# movie 도 list, detail 이렇게 간단하게 쓸 지?