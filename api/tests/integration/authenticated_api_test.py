from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AuthenticatedAPITestCase(TestCase):
    list_url = None

    def SetUp(self):
        self.user = User.objects.create_user(password='test', first_name='Test', last_name='User', username='test')
        self.client.login(username='test', password='test')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        super().setUp()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    """validar a necessidade de testar a autenticação da api"""
    def test_list_authenticated(self):
        response = self.client.get(reverse(f'{self.list_url}'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
