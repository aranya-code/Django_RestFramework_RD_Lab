from rest_framework import serializers
from passengers.models import Passengers

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = ['id', 'name','travelpoints']