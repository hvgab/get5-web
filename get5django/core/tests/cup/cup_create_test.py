from django.test import TestCase
from django.urls import reverse

class cupCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_cup_create_page(self):
        response = self.client.get(reverse('cup_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cup/cup_create.html')