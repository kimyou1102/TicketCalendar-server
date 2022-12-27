from django.db import models

# Create your models here.
class Ticket(models.Model):
    artist = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    performance_info = models.CharField(max_length=200, null=True, unique=True)
