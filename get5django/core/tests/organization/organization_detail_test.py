from django.test import TestCase
from django.urls import reverse

class organizationDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_organization_detail_page(self):
        response = self.client.get(reverse('organization_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'organization/organization_detail.html')