from django.http import request
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestCoreViews(TestCase):
    def setUp(self):
        client = Client()
        self.response = client.get('/advito/')
        super().setUp()

    def test_index_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_content_index_view(self):
        self.assertContains(self.response, 'Постов нет')