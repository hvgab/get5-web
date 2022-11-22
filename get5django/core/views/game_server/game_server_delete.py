from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from core.models import GameServer

class GameServerDeleteView(DeleteView):
    model = GameServer
    template_name = "game_server/game_server_delete.html"
    success_url = reverse_lazy('game_server_list')