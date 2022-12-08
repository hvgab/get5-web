from core.forms import MatchCreateForm
from core.models import Match
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class MatchUpdateView(UpdateView):
    model = Match
    # fields = "__all__"
    template_name = "match/match_update.html"
    success_url = reverse_lazy("match_list")
    form_class = MatchCreateForm
