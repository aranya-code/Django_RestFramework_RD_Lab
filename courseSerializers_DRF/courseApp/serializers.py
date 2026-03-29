from rest_framework import serializers
from courseApp.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def __str__(self):
        return Course.name