from django.test import TestCase
from django.urls import reverse

class TeamListTestCase(TestCase):
    def setUp(self):
        pass

    def test_team_list_page(self):
        response = self.client.get(reverse('team_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'team/team_list.html')