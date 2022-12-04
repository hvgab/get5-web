import logging

from core.models import GameServer
from core.services.a2s_info_service import A2sInfoService
from core.services.a2s_service import A2sService
from core.services.og_image_service import OgImageService
from django.views.generic import DetailView

logger = logging.getLogger(__name__)


class GameServerDetailDatabaseView(DetailView):
    model = GameServer
    template_name = "game_server/game_server_detail_database.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
