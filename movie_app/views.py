from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Afisha_project_2.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, \
    MovieReviewsSerializer, DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer
from movie_app.models import Director, Movie, Review

@api_view(['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')

        director = Director.objects.create(name=name)
        director.save()
        return Response(data={'messege': 'Data received!',
                        'director': DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def director_detail_api_view(requests, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail': 'director not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if requests.method == 'GET':
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data)
    elif requests.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif requests.method == 'PUT':
        serializer = DirectorValidateSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)

        director.name = serializer.validated_data.get('name')

        director.save()
        return Response(data={'messege': 'Data received!',
                              'director': DirectorSerializer(director).data})

@api_view(['GET', 'POST'])
def movies_list_api_view(requests):
    if requests.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif requests.method == 'POST':
        serializer = MovieValidateSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director = serializer.validated_data.get('director')

        movie = Movie.objects.create(title=title,
                                     description=description,
                                     duration=duration,
                                     director=director)
        movie.save()
        return Response(data={'messege': 'Data received!',
                        'movie': MovieSerializer(movie).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail_api_view(requests, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'detail': 'movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if requests.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif requests.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif requests.method == 'PUT':
        serializer = MovieValidateSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)

        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director = serializer.validated_data.get('director')

        movie.save()
        return Response(data={'messege': 'Data received!',
                              'movie': MovieSerializer(movie).data})

@api_view(['GET', 'POST'])
def reviews_list_api_view(requests):
    if requests.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif requests.method == 'POST':
        serializer = ReviewValidateSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        movie = serializer.validated_data.get('movie')
        stars = serializer.validated_data.get('stars')

        review = Review.objects.create(text=text,
                                       movie=movie,
                                       stars=stars)
        review.save()
        return Response(data={'messege': 'Data received!',
                        'review': ReviewSerializer(movie).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail_api_view(requests, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail': 'review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if requests.method == 'GET':
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data)
    elif requests.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif requests.method == 'PUT':
        serializer = ReviewValidateSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.movie = serializer.validated_data.get('movie')
        review.stars = serializer.validated_data.get('stars')

        review.save()
        return Response(data={'messege': 'Data received!',
                              'review': MovieSerializer(review).data})

@api_view(['GET'])
def movie_reviews_list_api_view(requests):
    movies = Movie.objects.all()
    serializer = MovieReviewsSerializer(movies, many=True)

    return Response(data=serializer.data)