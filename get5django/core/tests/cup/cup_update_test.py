from django.test import TestCase
from django.urls import reverse

class cupUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_cup_update_page(self):
        response = self.client.get(reverse('cup_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cup/cup_update.html')