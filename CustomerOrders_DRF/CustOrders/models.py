from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Orders(models.Model):
    product = models.CharField(max_length=20)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer,related_name='orders',on_delete=models.CASCADE)

    def __str__(self):
        return self.product
