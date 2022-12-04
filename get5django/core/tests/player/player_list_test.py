from django.test import TestCase
from django.urls import reverse

class playerListTestCase(TestCase):
    def setUp(self):
        pass

    def test_player_list_page(self):
        response = self.client.get(reverse('player_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_list.html')