from django.test import TestCase
from django.urls import reverse

class playerUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_player_update_page(self):
        response = self.client.get(reverse('player_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_update.html')