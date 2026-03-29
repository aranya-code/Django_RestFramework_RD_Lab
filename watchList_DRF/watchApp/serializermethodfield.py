from rest_framework import serializers
from .models import Movie

class MovieCustomSerializer(serializers.ModelSerializer):
    len_obj = serializers.SerializerMethodField

    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_len_obj(self, object):
        length = len(object.name)
        return length