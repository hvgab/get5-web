
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
            # Get
            info = a2s.info(address)
            # To Dict
            info_dict = {}
            for attr in dir(info):
                if attr.startswith('_'):
                    continue
                info_dict[attr] = getattr(info, attr)
        except socket.timeout as e:
            logger.warn('Info Timeout')
            info = None
        
        try:
            players = a2s.players(address)
            # To Dict
            players_dict = []
            for player in players:
                player_dict = {}
                for attr in dir(player):
                    if attr.startswith('_'):
                        continue
                    player_dict[attr] = getattr(player, attr)
                players_dict.append(player_dict)
            players = players_dict
        except socket.timeout as e:
            logger.warn('Players Timeout')
            players = None
        
        try:
            rules = a2s.rules(address)
        except socket.timeout as e:
            logger.warn('Rules Timeout')
            rules = None

        return {"info":info, "players":players, "rules":rules}