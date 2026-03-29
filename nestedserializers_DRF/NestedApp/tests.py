# tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from NestedApp.models import Author, Book


class AuthorBookAPITestCase(APITestCase):

    def setUp(self):
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        self.book1 = Book.objects.create(
            title="Book One",
            rating=5,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            rating=4,
            author=self.author1
        )

    # -------------------------
    # AUTHOR TESTS
    # -------------------------

    def test_get_all_authors(self):
        url = "/author/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_create_author(self):
        url = "/author/"
        data = {"name": "New Author"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 3)

    def test_get_single_author(self):
        url = f"/author/{self.author1.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Author One")

    def test_update_author(self):
        url = f"/author/{self.author1.id}/"
        data = {"name": "Updated Author"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author1.refresh_from_db()
        self.assertEqual(self.author1.name, "Updated Author")

    def test_delete_author(self):
        url = f"/author/{self.author1.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 1)

    # -------------------------
    # BOOK TESTS
    # -------------------------

    def test_get_all_books(self):
        url = "/book/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_create_book(self):
        url = "/book/"
        data = {
            "title": "New Book",
            "rating": 3,
            "author": self.author2.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_get_single_book(self):
        url = f"/book/{self.book1.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

    def test_update_book(self):
        url = f"/book/{self.book1.id}/"
        data = {
            "title": "Updated Book",
            "rating": 4,
            "author": self.author1.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        url = f"/book/{self.book1.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -------------------------
    # NESTED SERIALIZER TEST
    # -------------------------

    def test_author_with_books(self):
        url = f"/author/{self.author1.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("books", response.data)
        self.assertEqual(len(response.data["books"]), 2)

        # Check nested structure
        book = response.data["books"][0]
        self.assertIn("title", book)
        self.assertIn("rating", book)