from django.views.generic import DetailView

from core.models import Team


class TeamDetailView(DetailView):
    model = Team
    template_name = "team/team_detail.html"
