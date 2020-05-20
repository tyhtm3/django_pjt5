from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from django.db.models import Count
from .models import Movie, Genre
from datetime import datetime
from .serializers import GenreSerializer,MovieSerializer

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all().order_by('-vote_count')

    paginator = Paginator(movies,12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context={
        'movies' : movies,
        'page_obj' : page_obj
    }

    return render(request, 'movies/movie_list.html', context)

@login_required
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk= movie_pk)
    context={
        'movie':movie
    }
    return render(request, 'movies/detail.html', context)


def movie_like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk= movie_pk)
    flag = True

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        flag = False
    else:
        movie.like_users.add(user)
        flag =True
    message = '성공'
    count = movie.like_users.count()

    data={
        'message' : message,
        'flag' :flag,
        'count' : count
    }
    return JsonResponse(data)



@api_view(['GET'])
def recommend(request):
    if len(request.user.like_movies.values('genres')) ==0 :
    ## 다른거 좋아요 누른 적 있으면 같은 장르.
        temp = datetime.now().second % 19
        print(temp)
        arr= [10770,10752,10751,10749,10402,9648,878,99,80,53,37,36,35,28,27,18,16,14,12]
        genre = get_object_or_404(Genre, pk=arr[temp])
    else:
        genre_id = request.user.like_movies.values('genres').annotate(count=Count('genres'))[0].get('genres')
        genre = get_object_or_404(Genre, pk = genre_id)
    movies =Movie.objects.filter(genres=genre)
    serializer = MovieSerializer(movies, many =True)
    # data={
    #     'date' : date,
    #     'movie': serializer.data
    # }
    return Response(serializer.data)


