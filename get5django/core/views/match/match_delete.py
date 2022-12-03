from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from core.models import Match

class MatchDeleteView(DeleteView):
    model = Match
    template_name = "match/match_delete.html"
    success_url = reverse_lazy('match_list')