from django.shortcuts import render
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.http import Http404
# Create your views here.

class ItemViewSet(viewsets.ViewSet):

    def list(self, request):
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = InventorySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get_item(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            raise Http404
        
    
    def update(self, request, pk):
        item = self.get_item(pk)
        serializer = InventorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        item = self.get_item(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemByCategory(APIView):

    def get(self, request, category):            
        items = Inventory.objects.filter(category=category)
        serializer = InventorySerializer(items, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    
class ItemSorted(APIView):
    
    def get(self, request):
        items = Inventory.objects.all().order_by('-price')
        serializer = InventorySerializer(items, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)