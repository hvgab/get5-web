from django.views.generic import DetailView

from core.models import GameServer
from core.services.a2s_service import A2sService
from core.services.a2s_info_service import A2sInfoService
from core.services.og_image_service import OgImageService
import logging

logger = logging.getLogger(__name__)

class GameServerDetailView(DetailView):
    model = GameServer
    template_name = "game_server/game_server_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.debug(context['gameserver'])
        
        gameserver = context["gameserver"]

        info = A2sInfoService.execute({'address':f'{gameserver.url}:{gameserver.port}'})
        context['info'] = info

        context["a2s"] = A2sService.execute({'game_server': gameserver})

        map_name = info['map_name']
        if "/" in map_name:
            map_name = map_name.split('/')[1]
            logger.debug(map_name)

        context[f"{info['server_name']}_image"] = OgImageService.execute({'url':f'https://steamcommunity.com/sharedfiles/filedetails/?id={map_name}'})

        return context
    