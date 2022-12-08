import logging
import socket

import a2s
from core.models import GameServer
from django import forms
from service_objects.services import Service

logger = logging.getLogger(__name__)


class A2sService(Service):
    gameserver = forms.ModelChoiceField(GameServer.objects)
    # command = forms.TextInput()

    def process(self):
        logger.debug("executing a2s service")

        gameserver = self.cleaned_data["gameserver"]
        # command = self.cleaned_data['command']
        logger.debug("game server:")
        logger.debug(gameserver)

        if gameserver.internal_url is not None:
            address = (gameserver.internal_url, gameserver.port)
        else:
            address = (gameserver.url, gameserver.port)

        try:
            # Get
            info = a2s.info(address)
            # To Dict
            info_dict = {}
            for attr in dir(info):
                if attr.startswith("_"):
                    continue
                info_dict[attr] = getattr(info, attr)
        except socket.timeout as e:
            logger.warn("Info Timeout")
            info = None

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

        try:
            rules = a2s.rules(address)
        except socket.timeout as e:
            logger.warn("Rules Timeout")
            rules = None

        return {"info": info, "players": players, "rules": rules}
