from core.models import GameServer
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class GameServerUpdateView(UpdateView):
    model = GameServer
    fields = "__all__"
    template_name = "game_server/game_server_update.html"
    success_url = reverse_lazy("gameserver_list")
