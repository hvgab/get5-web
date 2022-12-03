from django.test import TestCase
from django.urls import reverse

class MatchListTestCase(TestCase):
    def setUp(self):
        pass

    def test_match_list_page(self):
        response = self.client.get(reverse('match_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'match/match_list.html')