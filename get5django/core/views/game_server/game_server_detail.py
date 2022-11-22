from django.views.generic import DetailView

from core.models import GameServer


class GameServerDetailView(DetailView):
    model = GameServer
    template_name = "game_server/game_server_detail.html"
