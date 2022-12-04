from django.test import TestCase
from django.urls import reverse

class playerDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_player_detail_page(self):
        response = self.client.get(reverse('player_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_detail.html')