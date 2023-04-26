from django.db import models

# Create your models here.
class User(models.Model):
    p_id = models.BigIntegerField(primary_key=True, unique=True, default=0)
    user_nickname = models.CharField(max_length=100, null=True)
    age_range = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)