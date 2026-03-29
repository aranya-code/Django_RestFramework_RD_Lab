from rest_framework.test import APITestCase
from rest_framework import status
from fvbApp.models import Student

class StudentAPITests(APITestCase):
    
    def setUp(self):
        """
        This method runs before every test. We use it to set up 
        initial data that our test cases will rely on.
        """
        self.student = Student.objects.create(
            id=1, 
            name="Alice", 
            score="85.50"
        )
        
        # Hardcoding the URLs based on your urls.py
        self.list_url = '/students/'
        self.detail_url = f'/students/{self.student.id}'

    # --- Tests for student_list view ---

    def test_get_student_list(self):
        """Test retrieving a list of all students."""
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Alice")

    def test_create_valid_student(self):
        """Test creating a new student with valid data."""
        data = {
            "id": 2, 
            "name": "Bob", 
            "score": "92.00"
        }
        response = self.client.post(self.list_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)
        self.assertEqual(response.data['name'], "Bob")

    def test_create_invalid_student(self):
        """Test creating a new student with missing/invalid data."""
        # 'name' is empty, which is invalid
        data = {
            "id": 3, 
            "name": "", 
            "score": "92.00"
        }
        response = self.client.post(self.list_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Student.objects.count(), 1) # Count should still be 1

    # --- Tests for student_detail view ---

    def test_get_valid_student_detail(self):
        """Test retrieving a single student that exists."""
        response = self.client.get(self.detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Alice")

    def test_get_invalid_student_detail(self):
        """Test retrieving a single student that does NOT exist."""
        response = self.client.get('/students/999')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_student(self):
        """Test completely updating an existing student."""
        data = {
            "id": 1, 
            "name": "Alice Updated", 
            "score": "88.00"
        }
        response = self.client.put(self.detail_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Refresh the instance from the database to confirm it updated
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, "Alice Updated")
        self.assertEqual(self.student.score, 88.00)

    def test_update_invalid_student(self):
        """Test updating a student with invalid data."""
        data = {
            "id": 1, 
            "name": "Alice", 
            "score": "1000.00" # Invalid: max_digits is 4, this is 6 digits total
        }
        response = self.client.put(self.detail_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_student(self):
        """Test deleting an existing student."""
        response = self.client.delete(self.detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)