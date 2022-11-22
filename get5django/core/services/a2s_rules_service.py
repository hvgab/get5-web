
from django import forms
from service_objects.services import Service
import a2s
import logging
from core.models import GameServer
import socket 

logger = logging.getLogger(__name__)

class A2sService(Service):
    game_server = forms.ModelChoiceField(GameServer.objects)
    # command = forms.TextInput()

    def process(self):
        logger.debug('executing a2s service')
        
        game_server = self.cleaned_data['game_server']
        # command = self.cleaned_data['command']
        logger.debug('game server:')
        logger.debug(game_server)
        
        address = (game_server.url, game_server.port)
        
        try:
            rules = a2s.rules(address)
        except socket.timeout as e:
            logger.warn('Rules Timeout')
            rules = None

        return rules