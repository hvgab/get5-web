from core.models import GameServer
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class GameServerCreateView(CreateView):
    model = GameServer
    fields = "__all__"
    template_name = "game_server/game_server_create.html"
    success_url = reverse_lazy("gameserver_list")
