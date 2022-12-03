from django.test import TestCase
from django.urls import reverse

class MatchUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_match_update_page(self):
        response = self.client.get(reverse('match_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'match/match_update.html')