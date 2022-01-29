from django.db import models
from authentication.models import User
from bootcamp.models import Bootcamp
# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    weeks = models.CharField(max_length=255)
    tuition = models.CharField(max_length=255)
    minimumSkill = models.CharField(max_length=255)
    scholarhipsAvailable = models.BooleanField(default=False)
    bootcamp = models.ForeignKey(to=Bootcamp, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
