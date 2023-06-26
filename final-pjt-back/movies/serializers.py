from rest_framework import serializers
from .models import Genre, Movie



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('genres',)
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieListSerializer(MovieSerializer):
    genres = serializers.SerializerMethodField()

    class Meta(MovieSerializer.Meta):
        model = Movie
        # fields = ('genres', 'title')
        fields = '__all__'
    
    def get_genres(self, instance):
        genres = instance.genres.all()
        return [{'id': genre.id, 'tmdb_genre_id': genre.tmdb_genre_id, 'name': genre.name} for genre in genres]