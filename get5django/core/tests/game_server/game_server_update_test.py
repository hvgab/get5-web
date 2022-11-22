from django.test import TestCase
from django.urls import reverse

class GameServerUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_game_server_update_page(self):
        response = self.client.get(reverse('game_server_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_server/game_server_update.html')