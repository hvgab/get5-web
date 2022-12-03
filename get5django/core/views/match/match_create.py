from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from core.forms import MatchCreateForm
from core.models import Match

class MatchCreateView(CreateView):
    model = Match
    # fields = '__all__'
    template_name = "match/match_create.html"
    success_url = reverse_lazy('match_list')
    form_class = MatchCreateForm