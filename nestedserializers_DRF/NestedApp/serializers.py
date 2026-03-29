from NestedApp.models import Author, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True,many=True)
    class Meta:
        model = Author
        fields ='__all__'


"""
# StringRelatedField
class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(read_only=True,many=True)
    class Meta:
        model = Author
        fields ='__all__'

#PrimaryKeyRelatedSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    class Meta:
        model = Author
        fields ='__all__'


#HyperLinkedRelatedSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedModelSerializer(read_only=True,many=True)
    class Meta:
        model = Author
        fields ='__all__'
"""
