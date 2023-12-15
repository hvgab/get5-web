from django.test import TestCase
from django.urls import reverse

class cupDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_cup_delete_page(self):
        response = self.client.get(reverse('cup_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cup/cup_delete.html')