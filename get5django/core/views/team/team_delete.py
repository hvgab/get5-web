from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from core.models import Team

class TeamDeleteView(DeleteView):
    model = Team
    template_name = "team/team_delete.html"
    success_url = reverse_lazy('team_list')