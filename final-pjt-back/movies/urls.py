from django.urls import path, include
from movies import views


app_name = 'movies'
urlpatterns = [
    path('movie_update/', views.movie_update),
    path('genre_update/', views.genre_update),
    path('top_100_movie_list/', views.top_100_movie_list),
    path('top_100_movie_list/<str:genre>/', views.top_100_movie_list),
    path('total_genre/', views.total_genre),
    path('movie_detail/<int:movie_id>/', views.movie_detail)
]
