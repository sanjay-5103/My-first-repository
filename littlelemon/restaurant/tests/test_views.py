# restaurant/tests/test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu

class MenuListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pasta", price="12.50", inventory=10)
        Menu.objects.create(title="Pizza", price="15.00", inventory=5)

    def test_list_returns_items(self):
        resp = self.client.get('/restaurant/menu/')   # <- прямой путь
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)
        self.assertEqual(resp.data[0]["title"], "Pasta")

class MenuDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_single_item(self):
        item = Menu.objects.create(title="Salad", price="7.00", inventory=20)
        resp = self.client.get(f'/restaurant/menu/{item.id}')  # <- прямой путь
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["title"], "Salad")
