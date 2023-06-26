from django.urls import path, include
from articles import views


app_name = 'articles'
urlpatterns = [
    path('article_list/', views.article_list),
    path('article_detail/<int:article_pk>/', views.article_detail),
]