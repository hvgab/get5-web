from core.models import Player
from django.views.generic import DetailView


class PlayerDetailView(DetailView):
    model = Player
    template_name = "player/player_detail.html"
