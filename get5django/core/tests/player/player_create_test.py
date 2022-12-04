from django.test import TestCase
from django.urls import reverse

class playerCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_player_create_page(self):
        response = self.client.get(reverse('player_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_create.html')