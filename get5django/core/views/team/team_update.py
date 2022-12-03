from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from core.models import Team

class TeamUpdateView(UpdateView):
    model = Team
    fields = '__all__'
    template_name = "team/team_update.html"
    success_url = reverse_lazy('team_list')
