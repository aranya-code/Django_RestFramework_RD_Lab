from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import ScoreCard


class ScoreCardAPITest(APITestCase):

    def setUp(self):
        self.player_data = {
            "player_name": "Virat Kohli",
            "jersey_no": 18,
            "technical_skill": "batter"
        }

        self.player = ScoreCard.objects.create(**self.player_data)

    # ---------------------------
    # CREATE PLAYER
    # ---------------------------
    def test_create_player(self):
        url = "/score/add/"
        data = {
            "player_name": "Rohit Sharma",
            "jersey_no": 45,
            "technical_skill": "batter"
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["player_name"], "Rohit Sharma")

    # ---------------------------
    # LIST PLAYERS
    # ---------------------------
    def test_list_players(self):
        url = "/score/list/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_list_players_empty(self):
        ScoreCard.objects.all().delete()
        url = "/score/list/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ---------------------------
    # GET PLAYER DETAIL
    # ---------------------------
    def test_get_player_detail(self):
        url = f"/score/detail/{self.player.jersey_no}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["jersey_no"], 18)

    def test_get_invalid_player(self):
        url = "/score/detail/999"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ---------------------------
    # UPDATE PLAYER (PARTIAL)
    # ---------------------------
    def test_update_player(self):
        url = f"/score/update/{self.player.jersey_no}"
        data = {
            "runs": 100
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["runs"], 100)

    def test_update_invalid_player(self):
        url = "/score/update/999"
        data = {"runs": 50}
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ---------------------------
    # DELETE PLAYER
    # ---------------------------
    def test_delete_player(self):
        url = f"/score/delete/{self.player.jersey_no}"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_player(self):
        url = "/score/delete/999"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)