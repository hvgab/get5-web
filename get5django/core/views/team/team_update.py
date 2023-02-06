import logging
from typing import Any, Dict

from core.models import Team
from core.services.steam_get_friends_service import SteamGetFriendsService
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

logger = logging.getLogger(__name__)


class TeamUpdateView(UpdateView):
    model = Team
    fields = "__all__"
    template_name = "team/team_update.html"
    success_url = reverse_lazy("team_list")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        steam_auth = self.request.user.social_auth.filter(provider="steam").first()
        try:
            steam_friends = SteamGetFriendsService.execute({"steam_id": steam_auth.uid})
        except:
            steam_friends = []
        context["steam_friends"] = steam_friends

        return context
