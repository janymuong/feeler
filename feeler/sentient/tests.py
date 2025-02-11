from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AuthTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.login_url = "/api/token/"

    def test_valid_login(self):
        response = self.client.post(self.login_url, {"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_invalid_login(self):
        response = self.client.post(self.login_url, {"username": "testuser", "password": "wrongpass"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class SentimentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.predict_url = "/api/predict/"
        self.client.login(username="testuser", password="testpass")
        self.token = self.client.post("/api/token/", {"username": "testuser", "password": "testpass"}).data["access"]

    def test_valid_prediction(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}
        data = {"text": "I love this app!"}
        response = self.client.post(
            self.predict_url, 
            data,
            format='json',
            **headers
        )
        
        print(f"Response Status: {response.status_code}")
        print(f"Response Data: {response.data if hasattr(response, 'data') else response.content}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("sentiment", response.data)
        self.assertIn("confidence", response.data)

    def test_invalid_input(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}
        response = self.client.post(
            self.predict_url, 
            {"text": ""}, 
            format='json',
            **headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)