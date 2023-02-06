import logging
import socket

import a2s
from core.models import GameServer
from django import forms
from service_objects.services import Service

logger = logging.getLogger(__name__)


class A2sPlayerService(Service):
    gameserver = forms.ModelChoiceField(GameServer.objects)

    def process(self):
        gameserver = self.cleaned_data["gameserver"]
        address = (gameserver.rcon_url, int(gameserver.port))

        try:
            players = a2s.players(address)
            # To Dict
            players_dict = []
            for player in players:
                player_dict = {}
                for attr in dir(player):
                    if attr.startswith("_"):
                        continue
                    player_dict[attr] = getattr(player, attr)
                players_dict.append(player_dict)
            players = players_dict
        except socket.timeout as e:
            logger.warn("Players Timeout")
            players = None

        return players
