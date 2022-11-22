from django.test import TestCase
from django.urls import reverse

class GameServerDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_game_server_delete_page(self):
        response = self.client.get(reverse('game_server_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_server/game_server_delete.html')