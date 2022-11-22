from django.views.generic import ListView

from core.models import GameServer

class GameServerListView(ListView):
    model = GameServer
    template_name = "game_server/game_server_list.html"
