from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from core.models import GameServer

class GameServerUpdateView(UpdateView):
    model = GameServer
    fields = '__all__'
    template_name = "game_server/game_server_update.html"
    success_url = reverse_lazy('game_server_list')
