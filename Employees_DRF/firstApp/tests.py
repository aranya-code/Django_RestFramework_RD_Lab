from django.test import TestCase, Client
from django.urls import reverse
from firstApp.models import emp

class TestEmpModel(TestCase):
    def setUp(self):
        # Create a test employee
        self.employee = emp.objects.create(id=1, name="Aranya", salary=3698000)

    def test_emp_creation_and_str(self):
        # Verify the data was saved correctly
        self.assertEqual(self.employee.name, "Aranya")
        self.assertEqual(self.employee.salary, 3698000)
        
        # Test the __str__ method of the model
        self.assertEqual(str(self.employee), "Aranya")


class TestEmployeeView(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a couple of employees in the test database
        emp.objects.create(id=1, name="Aranya", salary=3698000)
        emp.objects.create(id=2, name="John Doe", salary=85000)

    def test_employee_view_json_response(self):
        # Using name in path variable
        url = reverse('employee_list')
        response = self.client.get(url)

        # 1. Check that the request was successful
        self.assertEqual(response.status_code, 200)

        # 2. Extract the JSON payload from the response
        json_data = response.json()

        # 3. Verify the structure of the JSON (it should have a 'data' key)
        self.assertIn('data', json_data)
        
        # 4. Verify we got exactly 2 records back
        self.assertEqual(len(json_data['data']), 2)

        # 5. Verify the actual content matches what the view is supposed to return
        # (Notice we don't expect the 'id' field, because your view filters it out)
        expected_data = [
            {'name': 'Aranya', 'salary': 3698000},
            {'name': 'John Doe', 'salary': 85000}
        ]
        self.assertEqual(json_data['data'], expected_data)