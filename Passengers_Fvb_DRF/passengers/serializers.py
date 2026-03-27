from rest_framework import serializers
from passengers.models import Passengers

class PassengerSerializer(serializers.ModelSerializer):
    """
    Translates the Passenger model instances into JSON format (and vice versa).
    """
    # Serializing the model using ModelSerializer
    class Meta:
        model = Passengers
        fields = ['id', 'name','travelpoints']