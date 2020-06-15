from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # movies CRUD
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
]

# movie 도 list, detail 이렇게 간단하게 쓸 지?