from django.views.generic import ListView

from core.models import Team

class TeamListView(ListView):
    model = Team
    template_name = "team/team_list.html"
