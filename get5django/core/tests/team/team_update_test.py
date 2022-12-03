from django.test import TestCase
from django.urls import reverse

class TeamUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_team_update_page(self):
        response = self.client.get(reverse('team_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'team/team_update.html')