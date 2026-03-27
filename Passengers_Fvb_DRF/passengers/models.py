from django.db import models

class Passengers(models.Model):
    # Creating Passengers model
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    travelpoints = models.IntegerField()
