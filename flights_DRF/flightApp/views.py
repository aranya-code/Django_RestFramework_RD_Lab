from django.shortcuts import render
from flightApp.serializers import FlightSerializer, PassenegerSerializer, ReservationSerializer
from rest_framework import viewsets
from flightApp.models import Flight, Passenger, Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departureCity=request.data['departureCity'],
                                    arrivalCity=request.data['arrivalCity'],
                                    departureDate=request.data['departureDate'])
    serializer = FlightSerializer(flights, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_reservations(request):
    flight = Flight.objects.get(id = request.data['flightNumber'])

    passenger = Passenger()
    passenger.name = request.data['name']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save()

    return Response(status=status.HTTP_201_CREATED)



class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassenegerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
