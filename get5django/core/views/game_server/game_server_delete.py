from core.models import GameServer
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class GameServerDeleteView(DeleteView):
    model = GameServer
    template_name = "game_server/game_server_delete.html"
    success_url = reverse_lazy("gameserver_list")
