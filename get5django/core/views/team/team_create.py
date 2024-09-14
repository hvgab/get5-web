import logging
from pprint import pprint
from typing import Any, Dict

from core.models import Team
from core.services.steam_get_friends_service import SteamGetFriendsService
from core.services.steam_get_owned_games_service import SteamGetOwnedGamesService
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from social_django.models import UserSocialAuth
from unidecode import unidecode

logger = logging.getLogger(__name__)


class TeamCreateView(CreateView):
    model = Team
    fields = "__all__"
    template_name = "team/team_create.html"
    success_url = reverse_lazy("team_list")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        steam_auth = self.request.user.social_auth.filter(provider="steam").first()
        steam_friends = []
        try:
            steam_friends = SteamGetFriendsService.execute({"steam_id": steam_auth.uid})
        except:
            pass

        # Only get those who play cs2
        for i, friend in enumerate(steam_friends):
            owned_games = SteamGetOwnedGamesService.execute(
                {"steam_id": friend["steamid"]}
            )

            # print(owned_games)

            owns_cs2 = None
            if owned_games == None:
                # logger.debug("Cannot see profile and owned games.")
                owns_cs2 = None
            elif owned_games and 730 in owned_games:
                # logger.debug("730 in owned_games")
                owns_cs2 = True
            elif owned_games and 730 not in owned_games:
                # logger.debug("730 NOT in owned_games")
                owns_cs2 = False
            # logger.debug(f"owns_cs2? {owns_cs2}")
            steam_friends[i]["owns_cs2"] = owns_cs2

        for i, friend in enumerate(steam_friends):
            translit = unidecode(friend["personaname"])
            steam_friends[i]["translit"] = translit

        context["steam_friends"] = steam_friends

        return context
