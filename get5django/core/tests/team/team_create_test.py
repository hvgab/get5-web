from django.test import TestCase
from django.urls import reverse

class TeamCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_team_create_page(self):
        response = self.client.get(reverse('team_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'team/team_create.html')