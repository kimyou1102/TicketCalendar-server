from django.db import models

# Create your models here.
class Ticket(models.Model):
    artist = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=200)
    date_full = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=100)
    link = models.TextField(null=True)
    performance_info = models.CharField(max_length=300, unique=True, null=True)
