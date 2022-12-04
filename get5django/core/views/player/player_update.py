from core.models import Player
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class PlayerUpdateView(UpdateView):
    model = Player
    fields = "__all__"
    template_name = "player/player_update.html"
    success_url = reverse_lazy("player_list")
