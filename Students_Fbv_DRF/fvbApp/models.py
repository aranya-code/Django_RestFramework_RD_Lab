from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 50)
    score = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.name
