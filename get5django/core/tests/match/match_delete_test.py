from django.test import TestCase
from django.urls import reverse

class MatchDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_match_delete_page(self):
        response = self.client.get(reverse('match_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'match/match_delete.html')