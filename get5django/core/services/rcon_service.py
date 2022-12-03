
from django import forms
from service_objects.services import Service
from rcon.source import Client as RconClient
import logging
from core.models import GameServer
logger = logging.getLogger(__name__)

class RconService(Service):
    gameserver = forms.ModelChoiceField(GameServer.objects)
    command = forms.CharField()

    def process(self):
        
        print("\n\n\n")
        logger.debug("RconService Process")
        logger.debug(self.cleaned_data)

        gameserver = self.cleaned_data['gameserver']
        command = self.cleaned_data['command']
        
        with RconClient(gameserver.url, gameserver.port, passwd=gameserver.rcon_password) as client:
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