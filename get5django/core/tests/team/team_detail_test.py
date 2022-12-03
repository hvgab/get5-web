from django.test import TestCase
from django.urls import reverse

class TeamDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_team_detail_page(self):
        response = self.client.get(reverse('team_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'team/team_detail.html')