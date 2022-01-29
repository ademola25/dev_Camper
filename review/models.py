from django.db import models
from authentication.models import User
from bootcamp.models import Bootcamp
# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    bootcamp = models.ForeignKey(to=Bootcamp, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title
