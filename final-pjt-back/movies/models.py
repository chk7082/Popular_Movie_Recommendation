from django.db import models

# Create your models here.

class Genre(models.Model):
    tmdb_genre_id = models.IntegerField()
    name = models.CharField(max_length=20)


class Movie(models.Model):
    tmdb_movie_id = models.IntegerField()    # tmdb id
    adult = models.BooleanField()            # 성인영화 여부
    backdrop_path = models.TextField(null=True)       # tmdb 영화별 배경사진 경로
    original_title = models.CharField(max_length=100) # 영화 원제목
    overview = models.TextField()            # 개요
    popularity = models.DecimalField(max_digits=12, decimal_places=6) # TMDB에서 매긴 유명도 점수
    poster_path = models.TextField()         # 포스터 url
    release_date = models.CharField(max_length=15) # 개봉일
    runtime = models.SmallIntegerField()     # 영화 길이 (분)
    tagline = models.TextField(null=True)             # 짧은 소개 느낌
    title = models.CharField(max_length=100) # 영화 제목
    vote_average = models.DecimalField(max_digits=7, decimal_places=5) # 평균 평점
    vote_count = models.IntegerField()       # 평가자 수

    genres = models.ManyToManyField(Genre)   # 위 Genre와 묶인 ManyToMany Field

