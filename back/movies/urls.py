from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # moives
    path('', views.movie_list, name='movie_list'),
    # path('<int:movie_pk>/like/', views.movie_like, name='movie_like'),
]