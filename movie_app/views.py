from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Afisha_project_2.serializers import DirectorSerilizer, MovieSerilizer, ReviewSerilizer, \
    MovieReviewsSerilizer
from movie_app.models import Director, Movie, Review

@api_view(['GET', 'POST'])
def directors_list_api_view(requests):
    if requests.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerilizer(directors, many=True)
        return Response(data=serializer.data)
    elif requests.method == 'POST':
        name = requests.data.get('name')

        director = Director.objects.create(name=name)
        director.save()
        return Response(data={'messege': 'Data received!',
                        'director': DirectorSerilizer(director).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def director_detail_api_view(requests, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail': 'director not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if requests.method == 'GET':
        serializer = DirectorSerilizer(director, many=False)
        return Response(data=serializer.data)
    elif requests.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif requests.method == 'PUT':
        director.name = requests.data.get('name')

        director.save()
        return Response(data={'messege': 'Data received!',
                              'director': DirectorSerilizer(director).data})

@api_view(['GET', 'POST'])
def movies_list_api_view(requests):
    if requests.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerilizer(movies, many=True)
        return Response(data=serializer.data)
    elif requests.method == 'POST':
        title = requests.data.get('title')
        description = requests.data.get('description')
        duration = requests.data.get('duration')
        director = requests.data.get('director')

        movie = Movie.objects.create(title=title,
                                     description=description,
                                     duration=duration,
                                     director=director)
        movie.save()
        return Response(data={'messege': 'Data received!',
                        'movie': MovieSerilizer(movie).data},
                         status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail_api_view(requests, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'detail': 'movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if requests.method == 'GET':
        serializer = MovieSerilizer(movie, many=False)
        return Response(data=serializer.data)
    elif requests.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif requests.method == 'PUT':
        movie.title = requests.data.get('title')
        movie.description = requests.data.get('description')
        movie.duration = requests.data.get('duration')
        movie.director = requests.data.get('director')

        movie.save()
        return Response(data={'messege': 'Data received!',
                              'movie': MovieSerilizer(movie).data})

@api_view(['GET', 'POST'])
def reviews_list_api_view(requests):
    if requests.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerilizer(reviews, many=True)
        return Response(data=serializer.data)
    elif requests.method == 'POST':
        text = requests.data.get('text')
        movie = requests.data.get('movie')
        stars = requests.data.get('stars')

        review = Review.objects.create(text=text,
                                       movie=movie,
                                       stars=stars)
        review.save()
        return Response(data={'messege': 'Data received!',
                        'review': ReviewSerilizer(movie).data},
                         status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail_api_view(requests, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail': 'review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if requests.method == 'GET':
        serializer = ReviewSerilizer(review, many=False)
        return Response(data=serializer.data)
    elif requests.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif requests.method == 'PUT':
        review.text = requests.data.get('text')
        review.movie = requests.data.get('movie')
        review.stars = requests.data.get('stars')

        review.save()
        return Response(data={'messege': 'Data received!',
                              'review': MovieSerilizer(review).data})

@api_view(['GET'])
def movie_reviews_list_api_view(requests):
    movies = Movie.objects.all()
    serializer = MovieReviewsSerilizer(movies, many=True)

    return Response(data=serializer.data)