from core.models import Player
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class PlayerDeleteView(DeleteView):
    model = Player
    template_name = "player/player_delete.html"
    success_url = reverse_lazy("player_list")
