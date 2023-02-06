from core.models import Player
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class PlayerCreateView(CreateView):
    model = Player
    fields = "__all__"
    template_name = "player/player_create.html"
    success_url = reverse_lazy("player_list")
