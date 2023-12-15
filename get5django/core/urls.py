from core.views import (
    CupCreateView,
    CupDeleteView,
    CupDetailView,
    CupListView,
    CupUpdateView,
    GameServerCreateView,
    GameServerDeleteView,
    GameServerDetailA2sInfoView,
    GameServerDetailDatabaseView,
    GameServerDetailRconQueryView,
    GameServerDetailView,
    GameServerListView,
    GameServerUpdateView,
    MatchCreateView,
    MatchDeleteView,
    MatchDetailView,
    MatchListView,
    MatchUpdateView,
    OrganizationCreateView,
    OrganizationDeleteView,
    OrganizationDetailView,
    OrganizationListView,
    OrganizationUpdateView,
    PlayerCreateView,
    PlayerDeleteView,
    PlayerDetailView,
    PlayerListView,
    PlayerUpdateView,
    TeamCreateView,
    TeamDeleteView,
    TeamDetailView,
    TeamListView,
    TeamUpdateView,
)
from core.views.game_server.game_server_detail_index import GameServerDetailIndexView
from core.views.index import IndexView
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

gameserver_urlpatterns = [
    path(
        "",
        RedirectView.as_view(pattern_name="gameserver_list"),
        name="gameserver_index",
    ),
    path("list/", GameServerListView.as_view(), name="gameserver_list"),
    path(
        "create/",
        GameServerCreateView.as_view(),
        name="gameserver_create",
    ),
    path(
        "<int:pk>/",
        GameServerDetailIndexView.as_view(),
        name="gameserver_detail_index",
    ),
    path(
        "<int:pk>/update/",
        GameServerUpdateView.as_view(),
        name="gameserver_update",
    ),
    path(
        "<int:pk>/delete/",
        GameServerDeleteView.as_view(),
        name="gameserver_delete",
    ),
    path(
        "<int:pk>/detail",
        GameServerDetailDatabaseView.as_view(),
        name="gameserver_detail",
    ),
    path(
        "<int:pk>/rcon",
        GameServerDetailRconQueryView.as_view(),
        name="gameserver_rcon",
    ),
    path(
        "<int:pk>/a2s-info",
        GameServerDetailA2sInfoView.as_view(),
        name="gameserver_a2s_info",
    ),
]

team_urlpatterns = [
    path("", RedirectView.as_view(pattern_name="team_list"), name="team_index"),
    path("list/", TeamListView.as_view(), name="team_list"),
    path("create/", TeamCreateView.as_view(), name="team_create"),
    path("<int:pk>/", TeamDetailView.as_view(), name="team_detail"),
    path("<int:pk>/update/", TeamUpdateView.as_view(), name="team_update"),
    path("<int:pk>/delete/", TeamDeleteView.as_view(), name="team_delete"),
]

match_urlpatterns = [
    path("", RedirectView.as_view(pattern_name="match_list"), name="match_index"),
    path("list/", MatchListView.as_view(), name="match_list"),
    path("create/", MatchCreateView.as_view(), name="match_create"),
    path("<int:pk>/", MatchDetailView.as_view(), name="match_detail"),
    path("<int:pk>/update/", MatchUpdateView.as_view(), name="match_update"),
    path("<int:pk>/delete/", MatchDeleteView.as_view(), name="match_delete"),
]

player_urlpatterns = [
    path("", RedirectView.as_view(pattern_name="player_list"), name="player_index"),
    path("list/", PlayerListView.as_view(), name="player_list"),
    path("create/", PlayerCreateView.as_view(), name="player_create"),
    path("<int:pk>/detail/", PlayerDetailView.as_view(), name="player_detail"),
    path("<int:pk>/update/", PlayerUpdateView.as_view(), name="player_update"),
    path("<int:pk>/delete/", PlayerDeleteView.as_view(), name="player_delete"),
]

organization_urlpatterns = [
    path("list/", OrganizationListView.as_view(), name="organization_list"),
    path("create/", OrganizationCreateView.as_view(), name="organization_create"),
    path(
        "detail/<int:pk>/",
        OrganizationDetailView.as_view(),
        name="organization_detail",
    ),
    path(
        "update/<int:pk>/",
        OrganizationUpdateView.as_view(),
        name="organization_update",
    ),
    path(
        "delete/<int:pk>/",
        OrganizationDeleteView.as_view(),
        name="organization_delete",
    ),
]
cup_urlpatterns = [
    path("list/", CupListView.as_view(), name="cup_list"),
    path("create/", CupCreateView.as_view(), name="cup_create"),
    path("detail/<int:pk>/", CupDetailView.as_view(), name="cup_detail"),
    path("update/<int:pk>/", CupUpdateView.as_view(), name="cup_update"),
    path("delete/<int:pk>/", CupDeleteView.as_view(), name="cup_delete"),
]


urlpatterns = [
    # path("", RedirectView.as_view(pattern_name="gameserver_list"), name="index"),
    path("", IndexView.as_view(), name="index"),
    path("game-server/", include(gameserver_urlpatterns)),
    path("team/", include(team_urlpatterns)),
    path("match/", include(match_urlpatterns)),
    path("player/", include(player_urlpatterns)),
    path("cup/", include(cup_urlpatterns)),
    path("organization/", include(organization_urlpatterns)),
]
