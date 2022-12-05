from core.views import (
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
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

gameserver_urlpatterns = [
    path(
        "game-server",
        RedirectView.as_view(pattern_name="gameserver_list"),
        name="gameserver_index",
    ),
    path("game-server/list/", GameServerListView.as_view(), name="gameserver_list"),
    path(
        "game-server/create/", GameServerCreateView.as_view(), name="gameserver_create"
    ),
    path(
        "game-server/<int:pk>/",
        GameServerDetailView.as_view(),
        name="gameserver_detail",
    ),
    path(
        "game-server/<int:pk>/update/",
        GameServerUpdateView.as_view(),
        name="gameserver_update",
    ),
    path(
        "game-server/<int:pk>/delete/",
        GameServerDeleteView.as_view(),
        name="gameserver_delete",
    ),
    path(
        "game-server/<int:pk>/database",
        GameServerDetailDatabaseView.as_view(),
        name="gameserver_database",
    ),
    path(
        "game-server/<int:pk>/rcon",
        GameServerDetailRconQueryView.as_view(),
        name="gameserver_rcon",
    ),
    path(
        "game-server/<int:pk>/a2s-info",
        GameServerDetailA2sInfoView.as_view(),
        name="gameserver_a2s_info",
    ),
]

team_urlpatterns = [
    path("team/", RedirectView.as_view(pattern_name="team_list"), name="team_index"),
    path("team/list/", TeamListView.as_view(), name="team_list"),
    path("team/create/", TeamCreateView.as_view(), name="team_create"),
    path("team/<int:pk>/", TeamDetailView.as_view(), name="team_detail"),
    path("team/<int:pk>/update/", TeamUpdateView.as_view(), name="team_update"),
    path("team/<int:pk>/delete/", TeamDeleteView.as_view(), name="team_delete"),
]

match_urlpatterns = [
    path("match/", RedirectView.as_view(pattern_name="match_list"), name="match_index"),
    path("match/list/", MatchListView.as_view(), name="match_list"),
    path("match/create/", MatchCreateView.as_view(), name="match_create"),
    path("match/<int:pk>/", MatchDetailView.as_view(), name="match_detail"),
    path("match/<int:pk>/update/", MatchUpdateView.as_view(), name="match_update"),
    path("match/<int:pk>/delete/", MatchDeleteView.as_view(), name="match_delete"),
]

player_urlpatterns = [
    path(
        "player/", RedirectView.as_view(pattern_name="player_list"), name="player_index"
    ),
    path("player/list/", PlayerListView.as_view(), name="player_list"),
    path("player/create/", PlayerCreateView.as_view(), name="player_create"),
    path("player/<int:pk>/detail/", PlayerDetailView.as_view(), name="player_detail"),
    path("player/<int:pk>/update/", PlayerUpdateView.as_view(), name="player_update"),
    path("player/<int:pk>/delete/", PlayerDeleteView.as_view(), name="player_delete"),
]


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="gameserver_list"), name="index"),
]
urlpatterns += gameserver_urlpatterns
urlpatterns += team_urlpatterns
urlpatterns += match_urlpatterns
urlpatterns += player_urlpatterns
