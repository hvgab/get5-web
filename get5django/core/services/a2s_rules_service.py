import logging
import socket

import a2s
from core.models import GameServer
from django import forms
from service_objects.services import Service

logger = logging.getLogger(__name__)


class A2sRulesService(Service):
    gameserver = forms.ModelChoiceField(GameServer.objects)
    # command = forms.TextInput()

    def process(self):
        gameserver = self.cleaned_data["gameserver"]
        address = (gameserver.rcon_url, int(gameserver.port))

        try:
            rules = a2s.rules(address)
        except socket.timeout as e:
            logger.warn("Rules Timeout")
            rules = None

        return rules
