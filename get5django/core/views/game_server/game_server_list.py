from django.views.generic import ListView

from core.models import GameServer
import logging
from core.services.og_image_service import OgImageService
logger = logging.getLogger(__name__)

class GameServerListView(ListView):
    model = GameServer
    template_name = "game_server/game_server_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        for gameserver in context['gameserver_list']:
            
            gameserver.info = gameserver.get_info()

            # Map Image
            if gameserver.info is not None:
                map_name = gameserver.info['map_name']
                if "/" in map_name:
                    map_name = map_name.split('/')[1]
                    logger.debug(map_name)
                    gameserver.map_image = OgImageService.execute({'url':f'https://steamcommunity.com/sharedfiles/filedetails/?id={map_name}'})
                else:
                    gameserver.map_image = "https://static.wikia.nocookie.net/cswikia/images/1/1e/CSGO_Mirage_latest_version.jpg/revision/latest/scale-to-width-down/350?cb=20200301201524"

        return context
    