from django.test import TestCase
from django.urls import reverse

class cupDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_cup_detail_page(self):
        response = self.client.get(reverse('cup_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cup/cup_detail.html')