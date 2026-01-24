from django.db import models

class emp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name