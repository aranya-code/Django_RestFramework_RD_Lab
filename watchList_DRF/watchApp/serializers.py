from rest_framework import serializers
from watchApp.models import Movie, streamingPlatform, Reviews


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only = True)    
    class Meta:
        model = Reviews
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    len_obj = serializers.SerializerMethodField()
    Reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_len_obj(self, object):
        length = len(object.name)
        return length
    

class PlatformSerializer(serializers.ModelSerializer):
    Streaming_Partner = MovieSerializer(many = True, read_only = True)
    class Meta:
        model = streamingPlatform
        fields = '__all__'



    
"""

def description_length(value):
    if len(value)<5:
        raise serializers.ValidationError('The length is too low')
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators = [description_length])
    status = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    
    def validate_name(self, value):
        if len(value)<5:
            raise serializers.ValidationError('Name is too short')
        else:
            return value

    def validate(self, data):
        if data['name']==data['description']:
            raise serializers.ValidationError("Both fields can't be same")
        else:
            return data


"""
        
    
    