import logging

from core.models import GameServer
from core.services.a2s_info_service import A2sInfoService
from core.services.a2s_service import A2sService
from core.services.og_image_service import OgImageService
from django.views.generic import DetailView

logger = logging.getLogger(__name__)


class GameServerDetailView(DetailView):
    model = GameServer
    template_name = "game_server/game_server_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.debug(context["gameserver"])

        gameserver = context["gameserver"]

        context["info"] = A2sInfoService.execute(
            {"address": f"{gameserver.url}:{gameserver.port}"}
        )

        context["a2s"] = A2sService.execute({"game_server": gameserver})

        map_name = context["info"]["map_name"]
        if "/" in map_name:
            map_name = map_name.split("/")[1]
            logger.debug(map_name)

        if map_name == "de_dust2":
            map_name == "125438255"

        try:
            context[f'{context["info"]["server_name"]}_image'] = OgImageService.execute(
                {
                    "url": f"https://steamcommunity.com/sharedfiles/filedetails/?id={map_name}"
                }
            )
        except Exception as e:
            context[
                f'{context["info"]["server_name"]}_image'
            ] = "https://cdn1.dotesports.com/wp-content/uploads/2018/04/09112921/3473c60b-946a-4b95-bc8f-467919ace36f-800x450.jpg"

        return context
