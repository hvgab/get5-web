from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from core.models import Match

class MatchUpdateView(UpdateView):
    model = Match
    fields = '__all__'
    template_name = "match/match_update.html"
    success_url = reverse_lazy('match_list')
