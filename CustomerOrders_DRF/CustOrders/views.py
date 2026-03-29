from rest_framework import generics
from .serializers import CustomerSerializer, OrderSerializer
from .models import Customer, Orders
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = LimitOffsetPagination
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields= ['name','id']
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'id']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class= CustomerSerializer
    pagination_class = LimitOffsetPagination

class OrderList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    pagination_class = LimitOffsetPagination

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class= OrderSerializer
    pagination_class = LimitOffsetPagination