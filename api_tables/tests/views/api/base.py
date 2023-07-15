from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class AuthenticatedApiTestCase(APITestCase):
    def setUp(self):
        super().setUp()

        # Create and authenticate a user
        self.user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
