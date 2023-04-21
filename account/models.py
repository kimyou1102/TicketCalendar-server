from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigIntegerField(null=True)
    user_nickname = models.CharField(max_length=100, null=True)
    age_range = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)