from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'), # 디테일에서 코멘트 보여주기
    path('<int:review_pk>/create_comment/', views.create_comment, name='create_comment'),
]