from core.models import Player
from django.views.generic import ListView


class PlayerListView(ListView):
    model = Player
    template_name = "player/player_list.html"
