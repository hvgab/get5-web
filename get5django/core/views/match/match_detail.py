from django.views.generic import DetailView

from core.models import Match


class MatchDetailView(DetailView):
    model = Match
    template_name = "match/match_detail.html"
