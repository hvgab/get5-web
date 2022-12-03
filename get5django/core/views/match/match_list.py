from django.views.generic import ListView

from core.models import Match

class MatchListView(ListView):
    model = Match
    template_name = "match/match_list.html"
