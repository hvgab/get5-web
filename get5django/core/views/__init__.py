from .cup import CupCreateView, CupDeleteView, CupDetailView, CupListView, CupUpdateView
from .game_server import (
    GameServerCreateView,
    GameServerDeleteView,
    GameServerDetailA2sInfoView,
    GameServerDetailDatabaseView,
    GameServerDetailRconQueryView,
    GameServerDetailView,
    GameServerListView,
    GameServerUpdateView,
)
from .index import IndexView
from .match import (
    MatchCreateView,
    MatchDeleteView,
    MatchDetailView,
    MatchListView,
    MatchUpdateView,
)
from .organization import (
    OrganizationCreateView,
    OrganizationDeleteView,
    OrganizationDetailView,
    OrganizationListView,
    OrganizationUpdateView,
)
from .player import (
    PlayerCreateView,
    PlayerDeleteView,
    PlayerDetailView,
    PlayerListView,
    PlayerUpdateView,
)
from .team import (
    TeamCreateView,
    TeamDeleteView,
    TeamDetailView,
    TeamListView,
    TeamUpdateView,
)
