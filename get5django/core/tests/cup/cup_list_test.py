from django.test import TestCase
from django.urls import reverse

class cupListTestCase(TestCase):
    def setUp(self):
        pass

    def test_cup_list_page(self):
        response = self.client.get(reverse('cup_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cup/cup_list.html')