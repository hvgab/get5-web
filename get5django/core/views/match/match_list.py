from core.models import Match
from django.views.generic import ListView


class MatchListView(ListView):
    model = Match
    template_name = "match/match_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("match_date_time", "id")
