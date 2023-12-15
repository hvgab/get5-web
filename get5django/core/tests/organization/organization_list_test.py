from django.test import TestCase
from django.urls import reverse

class organizationListTestCase(TestCase):
    def setUp(self):
        pass

    def test_organization_list_page(self):
        response = self.client.get(reverse('organization_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'organization/organization_list.html')