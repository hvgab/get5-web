from django.test import TestCase
from django.urls import reverse

class organizationCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_organization_create_page(self):
        response = self.client.get(reverse('organization_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'organization/organization_create.html')