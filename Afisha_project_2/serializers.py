from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()

class ReviewSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class MovieSerilizer(serializers.ModelSerializer):
    movie_reviews = ReviewSerilizer(many=True)

    class Meta:
        model = Movie
        fields = 'id title description duration director movie_reviews'.split()

class MovieReviewsSerilizer(serializers.ModelSerializer):
    movie_reviews = ReviewSerilizer(many=True)

    class Meta:
        model = Movie
        fields = 'id title description duration director movie_reviews raiting'.split()
