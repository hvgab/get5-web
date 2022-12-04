from django.test import TestCase
from django.urls import reverse

class playerDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_player_delete_page(self):
        response = self.client.get(reverse('player_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player/player_delete.html')