from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from cbvApp.models import Student

class TestStudentAPI(APITestCase):
    def setUp(self):
        # Create a test student in the temporary test database
        self.student = Student.objects.create(id=1, name="John Doe", score=85)
        
        # Dynamically grab the URLs based on the names in urls.py
        self.list_url = reverse('students')
        self.detail_url = reverse('student_detail', kwargs={'pk': self.student.id})

    def test_get_student_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "John Doe")

    def test_create_student(self):
        data = {'id': 2, 'name': 'Jane Smith', 'score': 95}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)

    def test_get_single_student(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "John Doe")

    def test_update_student(self):
        data = {'id': 1, 'name': 'John Doe Updated', 'score': 90}
        response = self.client.put(self.detail_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Refresh from the DB to ensure the update actually saved
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, "John Doe Updated")
        self.assertEqual(self.student.score, 90)

    def test_delete_student(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)