from watchApp.models import Movie, streamingPlatform, Reviews
from watchApp.serializers import MovieSerializer, PlatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics


class MovieList(APIView):

    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetail(APIView):
    def get_pk(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        movie = self.get_pk(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        movie = self.get_pk(pk)
        serializer = MovieSerializer(movie, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        movie = self.get_pk(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlatformViewset(generics.ListCreateAPIView):
    queryset = streamingPlatform.objects.all()
    serializer_class = PlatformSerializer



class ReviewViewSet(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer



"""
@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method== 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method== 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):

    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""