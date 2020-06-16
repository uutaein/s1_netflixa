from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:user_pk>/', views.detail, name='detail'),
    # path('delete/', views.delete, name='delete'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    # path('<int:user_pk>/update/', views.update, name='update'),
    path('<str:user_name>/getname/', views.getname, name='getname')
]