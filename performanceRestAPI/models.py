from django.db import models
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=100, null=True)

class Ticket(models.Model):
    artist_id = models.ForeignKey(Artist, related_name="artist", on_delete=models.CASCADE, db_column="artist_id", null=True)
    artist = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=200)
    date_full = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=500, null=True)
    performance_info = models.CharField(max_length=300, unique=True, null=True)

