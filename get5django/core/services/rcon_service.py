
from django import forms
from service_objects.services import Service
from rcon.source import Client as RconClient
import logging

logger = logging.getLogger(__name__)

class RunRconService(Service):
    game_server = forms.ModelChoiceField('GameServer')
    command = forms.TextInput()

    def process(self):

        game_server = self.cleaned_data['game_server']
        command = self.cleaned_data['command']
        
        with RconClient(game_server.url, game_server.port, passwd=game_server.rcon_password) as client:
            logger.debug(command)
            logger.debug("\n")
            if isinstance(command, list):
                response = client.run(*command)
            else:
                response = client.run(command)
            logger.debug(response)
            logger.debug("\n\n")