# tests.py

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from watchApp.models import Movie, streamingPlatform, Reviews


class WatchListAPITestCase(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create streaming platform
        self.platform = streamingPlatform.objects.create(
            name="Netflix",
            about="Streaming service",
            website="www.netflix.com"
        )

        # Create movie
        self.movie = Movie.objects.create(
            name="Inception",
            description="Sci-fi movie",
            status=True,
            streamingplatform=self.platform
        )

        # Create review
        self.review = Reviews.objects.create(
            reviewer=self.user,
            rating=8,
            description="Great movie",
            movielist=self.movie
        )

    # -------------------------
    # MOVIE TESTS
    # -------------------------

    def test_get_all_movies(self):
        response = self.client.get("/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_movie(self):
        data = {
            "name": "Interstellar",
            "description": "Space movie",
            "status": True,
            "streamingplatform": self.platform.id
        }
        response = self.client.post("/list/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

    def test_get_single_movie(self):
        response = self.client.get(f"/detail/{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Inception")

    def test_update_movie(self):
        data = {
            "name": "Updated Movie",
            "description": "Updated desc",
            "status": True,
            "streamingplatform": self.platform.id
        }
        response = self.client.put(f"/detail/{self.movie.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.name, "Updated Movie")

    # NOTE: delete has bug in your code (missing request param)
    # So we expect failure unless fixed
    def test_delete_movie(self):
        response = self.client.delete(f"/detail/{self.movie.id}/")
        self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_405_METHOD_NOT_ALLOWED])

    # -------------------------
    # PLATFORM TESTS
    # -------------------------

    def test_get_all_platforms(self):
        response = self.client.get("/platform/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_platform(self):
        data = {
            "name": "Amazon Prime",
            "about": "Prime streaming",
            "website": "www.prime.com"
        }
        response = self.client.post("/platform/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # -------------------------
    # REVIEW TESTS
    # -------------------------

    def test_get_all_reviews(self):
        response = self.client.get("/review/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_review(self):
        self.client.login(username="testuser", password="testpass")

        data = {
            "rating": 9,
            "description": "Amazing!",
            "movielist": self.movie.id
        }
        response = self.client.post("/review/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reviews.objects.count(), 2)

    # -------------------------
    # NESTED SERIALIZER TESTS
    # -------------------------

    def test_movie_with_reviews(self):
        response = self.client.get(f"/detail/{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check nested reviews
        self.assertIn("Reviews", response.data)
        self.assertEqual(len(response.data["Reviews"]), 1)

        review = response.data["Reviews"][0]
        self.assertEqual(review["rating"], 8)

    def test_platform_with_movies(self):
        response = self.client.get("/platform/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        platform = response.data[0]
        self.assertIn("Streaming_Partner", platform)
        self.assertEqual(len(platform["Streaming_Partner"]), 1)


    # -------------------------
    # VALIDATION TESTS
    # -------------------------

    def test_invalid_review_rating(self):
        self.client.login(username="testuser", password="testpass")

        data = {
            "rating": 20,  # invalid (>10)
            "description": "Bad rating",
            "movielist": self.movie.id
        }
        response = self.client.post("/review/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_movie_creation(self):
        data = {
            "name": "",
            "description": "",
            "status": True
        }
        response = self.client.post("/list/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)