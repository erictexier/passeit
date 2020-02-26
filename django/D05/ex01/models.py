from django.db import models
from django.utils import timezone

# just as the recall to find out the django User table for admin...
#from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):

    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64, blank = False)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=32, blank = False)
    producer = models.CharField(max_length=128, blank = False)
    release_date = models.DateTimeField(blank = False)

    def __str__(self):
        return self.title