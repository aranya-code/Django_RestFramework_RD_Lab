from django.db import models

# Create your models here.
class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    barcode = models.IntegerField(unique=True)

