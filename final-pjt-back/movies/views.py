from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer

import requests

import os
import json
from pprint import pprint

# Create your views here.

# 기존에 있던 데이터는 넣지 않는 로직을 구현하지 않아서 한번만 실행하길 권장합니다
@api_view(['POST'])
def genre_update(request):
    # manage.py가 속해있는 폴더에 있는 secrets.json에서 TMDB API KEY를 가져오자
    secrets_path = os.path.join(os.getcwd(), 'secrets.json')
    with open(secrets_path) as f:
        secrets = json.loads(f.read())

    TMDB_API_KEY = secrets.get('TMDB_API_KEY')

    # https://developer.themoviedb.org/reference/genre-movie-list
    # 장르부터 업데이트
    genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR'

    # TMDB로부터 응답 받기
    response = requests.get(genre_url)
    genres = json.loads(response.text).get('genres')
    genres = [{'tmdb_genre_id': genre.get('id'), 'name': genre.get('name')} for genre in genres]

    # DB에 저장
    # GenreSerializer class의 method로 create 정의 (원래 있는데 덮어쓴 걸수도...?)
    for genre in genres:
        serializer = GenreSerializer()
        serializer.create(genre)
    
    return HttpResponse('')


# 기존에 있던 데이터는 넣지 않는 로직을 구현하지 않아서 한번만 실행하길 권장합니다
# 반드시 위의 genre_update를 실행하고 실행하길 권장합니다
@api_view(['POST'])
def movie_update(request):
    # popular movie 조회를 하면 한 페이지에 20개씩 데이터를 주는데
    # 몇 페이지 분량을 가져올 건지 결정
    num_of_pages = 20

    # manage.py가 속해있는 폴더에 있는 secrets.json에서 TMDB API KEY를 가져오자
    secrets_path = os.path.join(os.getcwd(), 'secrets.json')
    with open(secrets_path) as f:
        secrets = json.loads(f.read())

    TMDB_API_KEY = secrets.get('TMDB_API_KEY')

    popular_ids = []

    # 각 페이지를 순회하면서
    for page in range(1, num_of_pages+1):
        # https://developer.themoviedb.org/reference/movie-popular-list
        # 유명 영화들 get 요청으로 불러오기
        popular_url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&page={page}&language=ko-KR'

        # 원하는 데이터만 추출
        response = requests.get(popular_url)
        top_movies_in_this_page = json.loads(response.text).get('results')

        # 안의 영화들을 쭉 돌면서 id를 추출해서 popular_ids에 저장, 이를 통해서 추후에 TMDB에서 detail을 조회 => 이를 우리 데이터베이스에 저장하자
        for cur_movie in top_movies_in_this_page:
            cur_tmdb_id = cur_movie.get('id')
            popular_ids.append(cur_tmdb_id)

    # 각 추출한 영화 id들을 돌면서 상세정보를 조회하고 => 이를 우리 데이터베이스에 저장하자
    for popular_id in popular_ids:
        # https://developer.themoviedb.org/reference/movie-details
        # 영화 상세정보 get 요청으로 불러오기
        detail_url = f'https://api.themoviedb.org/3/movie/{popular_id}?api_key={TMDB_API_KEY}&language=ko-KR'
        response = requests.get(detail_url)
        cur_movie_detail = json.loads(response.text)

        # 원하는 정보만 추려내자
        info_we_need = {
             'tmdb_movie_id' : cur_movie_detail.get('id'),
                     'adult' : cur_movie_detail.get('adult'),
             'backdrop_path' : cur_movie_detail.get('backdrop_path'),
            'original_title' : cur_movie_detail.get('original_title'),
                  'overview' : cur_movie_detail.get('overview'),
                'popularity' : cur_movie_detail.get('popularity'),
               'poster_path' : cur_movie_detail.get('poster_path'),
              'release_date' : cur_movie_detail.get('release_date'),
                   'runtime' : cur_movie_detail.get('runtime'),
                   'tagline' : cur_movie_detail.get('tagline'),
                     'title' : cur_movie_detail.get('title'),
              'vote_average' : cur_movie_detail.get('vote_average'),
                'vote_count' : cur_movie_detail.get('vote_count'),
        }

        # print('#'*80)
        # pprint(info_we_need)
        # print('#'*80)

        serializer = MovieSerializer()
        serializer.create(info_we_need)

        # 지금 영화 인스턴스 불러오기 => 장르들을 ManyToMany field로 추가하려고
        this_movie = Movie.objects.get(tmdb_movie_id = info_we_need.get('tmdb_movie_id'))

        # 영화의 장르는 여러개로 분류될 수 있으니, 모두 순회하면서
        for cur_genre in cur_movie_detail.get('genres'):
            # 해당되는, 이미 저장되어 있는 장르 데이터를 가져와서
            this_genre = Genre.objects.get(tmdb_genre_id = cur_genre.get('id'))

            # Movie 데이터의 ManyToManyField인 Genres에 하나하나 연결
            this_movie.genres.add(this_genre)
    
    return HttpResponse('')


# dumpdata 시 python -Xutf8 manage.py dumpdata --indent 4 > data.json 이렇게 하면됨
# 불러올때 python manage.py loaddata data.json



@api_view(['GET'])
def top_100_movie_list(request, genre=None):
    # 만약 장르를 전달받지 않았다면
    # 장르 구분없이 탑 100 조회
    if not genre:
        movies = Movie.objects.all()

        # 100개 이상인 경우 100개만 짤라서
        if len(movies) > 100:
            movies = movies[:100]

        serializer = MovieListSerializer(many=True, instance=movies)

        return Response(serializer.data)

    # 특정 장르를 전달받았다면 => 그 장르에서 탑 100 조회 => 우리 데이터의 개수에 따라 100개가 없을수도
    else:
        # 장르 id를 추출
        genre_object = Genre.objects.get(name=genre)

        # 해당 장르를 가지고 있는 영화들 조회
        movies = genre_object.movie_set.all()
        
        # 100개 이상인 경우 100개만 짤라서
        if len(movies) > 100:
            movies = movies[:100]

        serializer = MovieListSerializer(many=True, instance=movies)
        
        return Response(serializer.data)

@api_view(['GET'])
def total_genre(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    serializer = MovieListSerializer(movie)
    return JsonResponse(serializer.data, safe=False)