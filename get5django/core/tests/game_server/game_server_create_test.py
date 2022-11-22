from django.test import TestCase
from django.urls import reverse

class GameServerCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_game_server_create_page(self):
        response = self.client.get(reverse('game_server_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_server/game_server_create.html')