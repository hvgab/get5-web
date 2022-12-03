
from django import forms
from service_objects.services import Service
from rcon.source import Client as RconClient
import logging
from core.models import GameServer
from django.conf import settings
import requests
from pprint import pformat

logger = logging.getLogger(__name__)

class SteamGetFriendsService(Service):
    
    steam_id = forms.CharField()

    
    def process(self):
        
        print("\n\n\n")
        logger.debug("Steam Get Friends Process")
        logger.debug(self.cleaned_data)

        steam_api_key = settings.SOCIAL_AUTH_STEAM_API_KEY
        steam_id = self.cleaned_data['steam_id']
        url = f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steam_api_key}&steamid={steam_id}&relationship=friend"

        r = requests.get(url)

        rj = r.json()

        # Get list of IDs
        steam_friend_ids = []
        for friend in rj['friendslist']['friends']:
            steam_friend_ids.append(friend['steamid'])

        # For each batch of 100 get summary.
        steam_friends_with_summary = []
        batch_size = 100
        for i in range(0, len(steam_friend_ids), batch_size):
            this_batch = steam_friend_ids[i:i+batch_size]
            steam_ids = ",".join(this_batch)
            url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steam_api_key}&steamids={steam_ids}"
            
            r = requests.get(url)

            logger.debug(pformat(r.json()))

            steam_friends_with_summary.extend(r.json()['response']['players'])

        return steam_friends_with_summary
