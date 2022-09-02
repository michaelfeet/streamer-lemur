from django.db import models

# Create your models here.

GENRES = (
    ('H', 'Horror'),
    ('S', 'Scify'),
    ('A', 'Action'),
    ('C', 'Comedy'),
    ('D', 'Drama'),
    ('R', 'Romance'),
    ('O', 'Rom Com'),
    ('T', 'Thriller'),
    ('M', 'Mystery'),
    ('F', 'Family'),
)

MPAA_RATINGS = (
    ('G', 'G'),
    ('P', 'PG'),
    ('1', 'PG-13'),
    ('R', 'R'),
    ('N', 'NC-17'),
    ('M', 'Mature Audience, Be Advised'),
)

class Media(models.Model):
    name = models.CharField(max_length=350)
    description = models.TextField(max_length=650)
    genre = models.CharField(
        max_length=1,
        choices=GENRES,
        default=GENRES[0][0]
    )
    mpaa_rating = models.CharField(
        max_length=1,
        choices=MPAA_RATINGS,
        default=MPAA_RATINGS[0][0]
    )
    