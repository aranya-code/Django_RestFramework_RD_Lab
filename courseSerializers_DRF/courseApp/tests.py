from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from courseApp.models import Course

class CourseAPITests(APITestCase):

    def setUp(self):
        """
        Runs before every test. We set up some initial data and URL paths.
        """
        # Create a sample course to test GET, PUT, and DELETE
        self.course = Course.objects.create(
            name="Django API Masterclass",
            description="Learn DRF from scratch.",
            rating=5
        )

        # Using reverse to dynamically fetch URLs based on the 'name' in urls.py
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', kwargs={'pk': self.course.pk})

    # --- Tests for CourseList APIView ---

    def test_get_course_list(self):
        """Test retrieving all courses."""
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Your custom response structure in views.py wraps data inside "data"
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "Data successfully processed!")
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]["name"], "Django API Masterclass")

    def test_create_course_valid(self):
        """Test creating a new course with valid data."""
        payload = {
            "name": "React Basics",
            "description": "Intro to React hooks.",
            "rating": 4
        }
        response = self.client.post(self.list_url, data=payload)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)
        self.assertEqual(response.data["name"], "React Basics")

    def test_create_course_invalid(self):
        """Test creating a new course with invalid data (missing required fields)."""
        payload = {
            "name": "", # Invalid: name is required and cannot be blank
            "description": "Testing invalid submission",
            "rating": 3
        }
        response = self.client.post(self.list_url, data=payload)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Course.objects.count(), 1) # Should still be 1 from setUp

    # --- Tests for CourseDetail APIView ---

    def test_get_course_detail_valid(self):
        """Test retrieving a specific course that exists."""
        response = self.client.get(self.detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Detail view does not wrap in "message" and "data", it returns serialized data directly
        self.assertEqual(response.data["name"], self.course.name)

    def test_get_course_detail_invalid(self):
        """Test retrieving a course that does not exist."""
        # Generating a URL for a primary key that doesn't exist
        invalid_url = reverse('detail', kwargs={'pk': 999})
        response = self.client.get(invalid_url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_course_valid(self):
        """Test updating a course."""
        payload = {
            "name": "Django API Masterclass (Updated)",
            "description": "Updated description.",
            "rating": 4
        }
        response = self.client.put(self.detail_url, data=payload)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Refresh the database instance to confirm changes applied
        self.course.refresh_from_db()
        self.assertEqual(self.course.name, "Django API Masterclass (Updated)")
        self.assertEqual(self.course.rating, 4)

    def test_delete_course(self):
        """Test deleting a course."""
        response = self.client.delete(self.detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)