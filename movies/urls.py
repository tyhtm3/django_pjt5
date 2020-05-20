from django.urls import path
from . import views
app_name = "movies"

urlpatterns = [
    path('', views.movie_list, name ='movie_list'),
    path('<int:movie_pk>/detail/', views.movie_detail, name ='movie_detail'),
    path('<int:movie_pk>/like/', views.movie_like, name ='movie_like'),
    path('recommend/', views.recommend, name ='recommend'),


]