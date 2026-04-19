import json
from django.test import TestCase, Client
from wishApp.models import Wish

class RestTestCase(TestCase):
    def setUp(self):
        # Set up a test client and some initial database records
        self.client = Client()
        self.wish1 = Wish.objects.create(title="Birthday", wishtext="Happy 20th Birthday!")
        self.wish2 = Wish.objects.create(title="Graduation", wishtext="Congrats on getting your degree!")
        
        self.list_url = '/wishes/'
        self.detail_url = f'/wishes/{self.wish1.id}/'
        self.invalid_detail_url = '/wishes/9999/'

    # --- TESTS FOR /wishes/ (GET, POST) ---

    def test_get_all_wishes(self):
        """Test retrieving all wishes"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        
        # Parse the JSON response
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['title'], "Birthday")

    def test_post_valid_wish(self):
        """Test creating a new wish with valid data"""
        payload = {
            "title": "New Job", 
            "wishtext": "Good luck on your first day!"
        }
        response = self.client.post(
            self.list_url, 
            data=json.dumps(payload), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Wish.objects.count(), 3)

    def test_post_invalid_wish(self):
        """Test creating a new wish with missing required fields (wishtext)"""
        payload = {
            "title": "Invalid Wish"
        }
        response = self.client.post(
            self.list_url, 
            data=json.dumps(payload), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    # --- TESTS FOR /wishes/<id>/ (GET, PUT, DELETE) ---

    def test_get_single_wish(self):
        """Test retrieving a specific wish by ID"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.content)
        self.assertEqual(data['title'], "Birthday")

    def test_get_nonexistent_wish(self):
        """Test retrieving a wish that doesn't exist returns a 404"""
        response = self.client.get(self.invalid_detail_url)
        self.assertEqual(response.status_code, 404)

    def test_put_valid_wish(self):
        """Test updating an existing wish"""
        payload = {
            "title": "Updated Birthday", 
            "wishtext": "Happy 21st Birthday!"
        }
        response = self.client.put(
            self.detail_url, 
            data=json.dumps(payload), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        # Refresh the database object to check if it actually updated
        self.wish1.refresh_from_db()
        self.assertEqual(self.wish1.title, "Updated Birthday")
        self.assertEqual(self.wish1.wishtext, "Happy 21st Birthday!")

    def test_put_invalid_wish(self):
        """Test updating a wish with invalid data"""
        payload = {
            "title": "Updated Title Only"
            # Missing wishtext
        }
        response = self.client.put(
            self.detail_url, 
            data=json.dumps(payload), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_wish(self):
        """Test deleting a wish"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        
        # Ensure the wish was actually removed from the database
        self.assertEqual(Wish.objects.count(), 1)