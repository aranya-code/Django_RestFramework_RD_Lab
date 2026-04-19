from django.db import models

class Wish(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True,default='')
    wishtext = models.TextField()

    class Meta:
        ordering = ('created',)
