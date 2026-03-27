from django.db import models

class Student(models.Model):
    # Creating Student model
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True, default='Aranya')
    score = models.IntegerField()

    def __str__(self):
        return self.name