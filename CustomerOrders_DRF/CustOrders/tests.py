import base64
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from CustOrders.models import Customer, Orders # Adjust 'CustOrders' if your app folder is named differently

class CustomerOrdersAPITests(APITestCase):

    def setUp(self):
        """
        Runs before every test. Sets up a user for authentication, 
        initial model instances, and URL paths.
        """
        # 1. Set up a User for BasicAuthentication
        self.user = User.objects.create_user(username='admin', password='testpassword123')
        
        # Create the Basic Auth header manually
        auth_string = f"{self.user.username}:testpassword123"
        encoded_auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
        self.auth_header = f'Basic {encoded_auth}'

        # 2. Set up initial data
        self.customer = Customer.objects.create(name="Alice Smith", phone="1234567890")
        self.order = Orders.objects.create(product="Mechanical Keyboard", quantity=2, customer=self.customer)

        # 3. Define endpoints
        self.customer_url = '/customer/'
        self.customer_detail_url = f'/customer/{self.customer.id}'
        self.order_url = '/order/'
        self.order_detail_url = f'/order/{self.order.id}'

    # --- CustomerList Tests ---

    def test_get_customer_list_unauthenticated(self):
        """Test that unauthenticated requests are blocked on CustomerList."""
        response = self.client.get(self.customer_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_customer_list_authenticated(self):
        """Test retrieving customers with proper Basic Authentication."""
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        response = self.client.get(self.customer_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Because of LimitOffsetPagination, data is wrapped in 'results'
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "Alice Smith")
        # Ensure the nested OrderSerializer is returning data properly
        self.assertEqual(len(response.data['results'][0]['orders']), 1)

    def test_search_customers(self):
        """Test the SearchFilter functionality on CustomerList."""
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        # Create a second customer to test filtering
        Customer.objects.create(name="Bob Jones", phone="0987654321")

        # Search for 'Bob'
        response = self.client.get(self.customer_url + '?search=Bob')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "Bob Jones")

    def test_create_customer(self):
        """Test creating a new customer."""
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        payload = {"name": "Charlie", "phone": "5555555555"}
        response = self.client.post(self.customer_url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)

    # --- CustomerDetail Tests ---

    def test_get_customer_detail(self):
        """Test retrieving a specific customer."""
        response = self.client.get(self.customer_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Alice Smith")

    def test_update_customer(self):
        """Test updating a customer."""
        payload = {"name": "Alice Smith Updated", "phone": "1111111111"}
        response = self.client.put(self.customer_detail_url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, "Alice Smith Updated")

    def test_delete_customer_cascades(self):
        """Test deleting a customer and verifying the CASCADE delete on orders."""
        response = self.client.delete(self.customer_detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
        # The order should also be deleted because of on_delete=models.CASCADE
        self.assertEqual(Orders.objects.count(), 0)

    # --- Order Endpoints Tests ---

    def test_get_order_list(self):
        """Test retrieving the paginated list of orders."""
        response = self.client.get(self.order_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['product'], "Mechanical Keyboard")

    def test_create_order(self):
        """Test creating a new order linked to a customer."""
        payload = {
            "product": "Gaming Mouse", 
            "quantity": 1, 
            "customer": self.customer.id
        }
        response = self.client.post(self.order_url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Orders.objects.count(), 2)

    def test_update_order(self):
        """Test updating an order's quantity."""
        payload = {
            "product": "Mechanical Keyboard", 
            "quantity": 5, 
            "customer": self.customer.id
        }
        response = self.client.put(self.order_detail_url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.quantity, 5)

    def test_delete_order(self):
        """Test deleting a single order."""
        response = self.client.delete(self.order_detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Orders.objects.count(), 0)
        # Verify the customer still exists (reverse cascade doesn't happen)
        self.assertEqual(Customer.objects.count(), 1)