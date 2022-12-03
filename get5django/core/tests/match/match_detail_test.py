from django.test import TestCase
from django.urls import reverse

class MatchDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_match_detail_page(self):
        response = self.client.get(reverse('match_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'match/match_detail.html')