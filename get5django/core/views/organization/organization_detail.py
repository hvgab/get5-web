from core.models import Organization
from django.views.generic import DetailView


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organization/organization_detail.html"
