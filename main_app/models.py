from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

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
    ('N', 'No')
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
    action_genre = models.BooleanField()
    anime = models.BooleanField()
    cartoon = models.BooleanField()
    comedy = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    family = models.BooleanField()
    fantasy = models.BooleanField()
    horror = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    scifi = models.BooleanField()
    thriller = models.BooleanField()
    mpaa_rating = models.CharField(
        max_length=1,
        choices=MPAA_RATINGS,
        default=MPAA_RATINGS[0][0]
     )
    
    netflix = models.BooleanField()
    amazon_prime = models.BooleanField()
    disney_plus = models.BooleanField()
    funimation = models.BooleanField()
    hulu = models.BooleanField()
    hbo_max = models.BooleanField()
    peacock = models.BooleanField()
    crunchyroll = models.BooleanField()
    paramount_plus = models.BooleanField()
    apple_tv_plus = models.BooleanField()
    movie = models.CharField(
        max_length=1,
        choices=YES_NO,
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
    last_episode_watched = models.CharField(
        max_length=100,
        default='N/A'
    )
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
    def get_absolute_url(self):
        return reverse('journals_detail', kwargs={'journal_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length= 200)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for media_id: {self.media_id} @{self.url}'