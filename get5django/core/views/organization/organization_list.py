from core.models import Organization
from django.views.generic import ListView


class OrganizationListView(ListView):
    model = Organization
    template_name = "organization/organization_list.html"
