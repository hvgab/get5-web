import logging
from pprint import pformat

import requests
from core.models import GameServer
from django import forms
from django.conf import settings
from django.core.cache import cache
from rcon.source import Client as RconClient
from service_objects.services import Service

logger = logging.getLogger(__name__)


class SteamGetOwnedGamesService(Service):

    steam_id = forms.CharField()

    def process(self):

        print("\n\n\n")
        logger.debug("Steam Get Owned Games Process")
        logger.debug(self.cleaned_data)

        steam_api_key = settings.SOCIAL_AUTH_STEAM_API_KEY
        steam_id = self.cleaned_data["steam_id"]

        cache_key = f"steam_get_owned_games_{steam_id}"
        appids = cache.get(cache_key)
        if appids is not None:
            return appids

        url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steam_api_key}&steamid={steam_id}&format=json"

        r = requests.get(url)

        rj = r.json()

        appids = []
        if "games" in rj["response"]:
            for game in rj["response"]["games"]:
                appids.append(game["appid"])

            cache.set(cache_key, appids, 1 * 60 * 60 * 24)  # one day
            return appids

        return None
