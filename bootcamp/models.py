from django.db import models
import uuid
from authentication.models import User
import os
from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.fields import ArrayField



def bootcamp_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/bootcamp/', filename)

# Create your models here.
class Bootcamp(models.Model):
    """Bootcamp model"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    website = models.URLField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=225, unique=True)
    address = models.CharField(max_length=255)
    careers = ArrayField(models.CharField(max_length=10, blank=True),size=8)
    averageRating = IntegerRangeField()
    averageCost = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(null=True, upload_to=bootcamp_image_file_path)
    housing = models.BooleanField(default=False)
    jobAssitance= models.BooleanField(default=False)
    jobGuarantee = models.BooleanField(default=False)
    acceptGi = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug
