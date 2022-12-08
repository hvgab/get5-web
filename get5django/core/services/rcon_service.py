import logging

from core.models import GameServer
from django import forms
from rcon.source import Client as RconClient
from service_objects.services import Service

logger = logging.getLogger(__name__)


class RconService(Service):
    gameserver = forms.ModelChoiceField(GameServer.objects)
    command = forms.CharField()

    def process(self):

        print("\n\n\n")
        logger.debug("RconService Process")
        logger.debug(self.cleaned_data)

        gameserver = self.cleaned_data["gameserver"]
        command = self.cleaned_data["command"]

        if gameserver.internal_url is not None:
            url = gameserver.internal_url
        else:
            url = gameserver.url

        with RconClient(
            url, gameserver.port, passwd=gameserver.rcon_password
        ) as client:
            logger.debug(command)
            logger.debug("\n")
            if isinstance(command, list):
                response = client.run(*command)
            else:
                response = client.run(command)
            logger.debug(response)
            logger.debug("\n\n")

            logger.debug(type(response))

            return response
