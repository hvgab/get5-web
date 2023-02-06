import logging
import socket

import a2s
from core.models import GameServer
from django import forms
from service_objects.services import Service

logger = logging.getLogger(__name__)


class A2sInfoService(Service):
    gameserver = forms.ModelChoiceField(GameServer.objects)

    def process(self):
        gameserver = self.cleaned_data["gameserver"]
        address = (gameserver.rcon_url, int(gameserver.port))

        try:
            # Get
            info = a2s.info(address)
            # To Dict
            info_dict = {}
            for attr in dir(info):
                if attr.startswith("_"):
                    continue
                info_dict[attr] = getattr(info, attr)
            info = info_dict
        except socket.timeout as e:
            logger.warn("Info Timeout")
            info = None

        return info
