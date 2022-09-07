from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

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
    ('O', 'Not Rated')
)

YES_NO = (
    ('Y', "Yes"),
    ('N', 'NO')
)

STREAMING = (
    ('N', 'Netflix'),
    ('A', 'Amazon Prime'),
    ('D', 'Disney'),
    ('F', 'Funimation'),
    ('H', 'Hulu'),
    ('B', 'HBO Max'),
    ('P', 'Peacock'),
    ('C', 'Crunchyroll'),
    ('M', 'Paramount+'),
    ('T', 'Apple TV+')
)
class Media(models.Model):
    name = models.CharField(max_length=350)
    description = models.TextField(max_length=650)
    genre = models.CharField(
        max_length=1,
        choices=GENRES,
        default=GENRES[0][0]
    )
    netflix = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    amazon_prime = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    disney_plus = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    funimation = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    hulu = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    hbo_max = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    peacock = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    crunchyroll = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    paramount_plus = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    apple_tv_plus = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    mpaa_rating = models.CharField(
        max_length=1,
        choices=MPAA_RATINGS,
        default=MPAA_RATINGS[0][0]
    )

    def get_absolute_url(self):
        return reverse('media_detail', kwargs={'pk': self.id})





class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    # media = models.
    where_am_i_watching = models.CharField(
        max_length=1,
        choices=STREAMING,
        default=STREAMING[0][0]
    )

    last_date_watched = models.DateField()
    continue_watching = models.CharField(
        max_length=1,
        choices=YES_NO,
    )
    completed_watching = models.CharField(
        max_length=1,
        choices=YES_NO,

    )
    would_watch_again = models.CharField(
        max_length=1,
        choices=YES_NO,

    )
    movie = models.CharField(
        max_length=1,
        choices=YES_NO,

    )

    def get_absolute_url(self):
        return reverse('journals_detail', kwargs={'journal_id': self.id})