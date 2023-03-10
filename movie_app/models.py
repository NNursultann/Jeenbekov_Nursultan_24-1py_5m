from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def movie_count(self):
        try:
            return Movie.objects.all().count()
        except:
            return ''

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def raiting(self):
        try:
            count = self.movie_reviews.all().count()
            stars = sum([i.stars for i in self.movie_reviews.all()])
            return stars // count
        except:
            return ''

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True,
                              related_name='movie_reviews')
    stars = models.IntegerField(choices=(
        (0, ''),
        (1, '*'),
        (2, '* *'),
        (3, '* * *'),
        (4, '* * * *'),
        (5, '* * * * *'),
    ), default=0)
