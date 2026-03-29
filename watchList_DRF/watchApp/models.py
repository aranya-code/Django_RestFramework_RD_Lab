from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class streamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    streamingplatform = models.ForeignKey(streamingPlatform, on_delete=models.CASCADE, related_name= 'Streaming_Partner', null=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    movielist = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='Reviews', null=True)

