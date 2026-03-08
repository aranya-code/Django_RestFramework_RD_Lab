from rest_framework import serializers
from cbvApp.models import Student


class StudentSerializers(serializers.ModelSerializer):
    # Serializing the students model
    class Meta:
        model = Student
        fields = '__all__'