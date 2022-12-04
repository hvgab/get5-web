import logging
from pprint import pformat

import requests
from core.models import GameServer
from django import forms
from django.conf import settings
from rcon.source import Client as RconClient
from service_objects import fields
from service_objects.services import Service

logger = logging.getLogger(__name__)


class SteamGetPlayerSummaryService(Service):

    steam_ids = fields.ListField()

    def process(self):

        print("\n\n\n")
        logger.debug("Steam Get Player Summary Process")
        logger.debug(self.cleaned_data)

        steam_api_key = settings.SOCIAL_AUTH_STEAM_API_KEY
        steam_ids = self.cleaned_data["steam_ids"]

        # For each batch of 100 get summary.
        players = []
        batch_size = 100
        for i in range(0, len(steam_ids), batch_size):
            this_batch = steam_ids[i : i + batch_size]
            steam_ids = ",".join(this_batch)
            url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steam_api_key}&steamids={steam_ids}"

            r = requests.get(url)

            logger.debug(pformat(r.json()))

            players.extend(r.json()["response"]["players"])

        return players
