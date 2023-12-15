from core.models import Organization
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "organization/organization_delete.html"
    success_url = reverse_lazy("organization_list")
