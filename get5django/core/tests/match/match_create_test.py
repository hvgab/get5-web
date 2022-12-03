from django.test import TestCase
from django.urls import reverse

class MatchCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_match_create_page(self):
        response = self.client.get(reverse('match_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'match/match_create.html')