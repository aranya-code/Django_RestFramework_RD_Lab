from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from passengers.models import Passengers
from passengers.serializers import PassengerSerializer

class TestPassengerModel(APITestCase):
    def test_passenger_creation(self):
        passenger = Passengers.objects.create(id=1, name="John Doe", travelpoints=1500)
        self.assertEqual(passenger.name, "John Doe")
        self.assertEqual(passenger.travelpoints, 1500)
        self.assertEqual(Passengers.objects.count(), 1)


class TestPassengerSerializer(APITestCase):
    def test_valid_serializer(self):
        data = {'id': 2, 'name': 'Jane Smith', 'travelpoints': 3000}
        serializer = PassengerSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer_missing_data(self):
        data = {'id': 3}
        serializer = PassengerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)


class TestPassengerViews(APITestCase):
    def setUp(self):
        # Create a test passenger to use in our view tests
        self.passenger = Passengers.objects.create(id=10, name="Alice", travelpoints=500)
        
        # Using reverse() dynamically based on your updated urls.py!
        self.list_url = reverse('passenger_list')
        self.detail_url = reverse('passenger_detail', kwargs={'pk': self.passenger.id})

    def test_get_passenger_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Alice")

    def test_post_valid_passenger(self):
        data = {'id': 11, 'name': 'Bob', 'travelpoints': 1200}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Passengers.objects.count(), 2)

    def test_get_passenger_detail_valid(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Alice")

    def test_get_passenger_detail_invalid(self):
        # Test a 404 response for an ID that doesn't exist
        invalid_url = reverse('passenger_detail', kwargs={'pk': 999})
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_passenger_detail(self):
        data = {'id': 10, 'name': 'Alice Updated', 'travelpoints': 800}
        response = self.client.put(self.detail_url, data, format='json')
        
        # Testing for 201 Created to match the logic exactly as written in your views.py
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Refresh the database instance and check if it actually updated
        self.passenger.refresh_from_db()
        self.assertEqual(self.passenger.name, 'Alice Updated')
        self.assertEqual(self.passenger.travelpoints, 800)

    def test_delete_passenger(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Passengers.objects.count(), 0)