from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title description duration director movie_reviews'.split()

class MovieReviewsSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title description duration director movie_reviews raiting'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    duration = serializers.DurationField()
    director_id = serializers.ListSerializer(child=serializers.IntegerField())

    def validate_director(self, director):
        try:
            Director.objects.get(id=director)
        except Director.DoesNotExist:
            raise ValidationError('This director does not exists!')
        return director

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    movie = serializers.ListSerializer(child=serializers.IntegerField())

    def validate_movie(self, movie):
        try:
            Director.objects.get(id=movie)
        except Director.DoesNotExist:
            raise ValidationError('This movie does not exists!')
        return movie