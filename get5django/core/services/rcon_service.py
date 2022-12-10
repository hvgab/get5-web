import logging
import socket

from core.models import GameServer
from django import forms
from rcon.source import Client as RconClient
from service_objects.services import Service

logger = logging.getLogger(__name__)


class RconService(Service):
    gameserver = forms.ModelChoiceField(GameServer.objects)
    command = forms.CharField()

    def process(self):
        gameserver = self.cleaned_data["gameserver"]
        command = self.cleaned_data["command"]

        try:
            with RconClient(
                gameserver.rcon_url,
                gameserver.port,
                passwd=gameserver.rcon_password,
                timeout=1.5,
            ) as client:
                if isinstance(command, list):
                    response = client.run(*command)
                else:
                    response = client.run(command)
                logger.debug(response)
                return response
        except socket.timeout as timeout:
            logger.error(timeout)
