from django.test import TestCase
from django.urls import reverse

class organizationUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_organization_update_page(self):
        response = self.client.get(reverse('organization_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'organization/organization_update.html')