from rest_framework import serializers
from .models import Customer, Orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(read_only = True, many=True)
    class Meta:
        model = Customer
        fields = '__all__'