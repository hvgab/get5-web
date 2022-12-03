from typing import Any, Dict
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from social_django.models import UserSocialAuth
from core.models import Team
from core.services.steam_get_friends_service import SteamGetFriendsService
import logging

logger = logging.getLogger(__name__)

class TeamCreateView(CreateView):
    model = Team
    fields = '__all__'
    template_name = "team/team_create.html"
    success_url = reverse_lazy('team_list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        logger.debug('request.user')
        logger.debug(self.request.user)
        
        logger.debug('STEAM FIRST')
        logger.debug(self.request.user.social_auth.filter(provider='steam').first())
        
        steam_auth = self.request.user.social_auth.filter(provider='steam').first()
        
        steam_friends = SteamGetFriendsService.execute({'steam_id': steam_auth.uid})

        context['steam_friends'] = steam_friends
        
        return context