from core.views import MatchDeleteView
from core.views import MatchUpdateView
from core.views import MatchDetailView
from core.views import MatchCreateView
from core.views import MatchListView
from core.views import TeamDeleteView
from core.views import TeamUpdateView
from core.views import TeamDetailView
from core.views import TeamCreateView
from core.views import TeamListView
from core.views import GameServerDeleteView
from core.views import GameServerUpdateView
from core.views import GameServerDetailView
from core.views import GameServerCreateView
from core.views import GameServerListView
from core.views import GameServerDetailRconQueryView

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView


gameserver_urlpatterns = [
    path('game-server', RedirectView.as_view(pattern_name='gameserver_list'), name='gameserver_index'),
    path('game-server/list/', GameServerListView.as_view(), name='gameserver_list'),
    path('game-server/create/', GameServerCreateView.as_view(), name='gameserver_create'),
    path('game-server/<int:pk>/detail/', GameServerDetailView.as_view(), name='gameserver_detail'),
    path('game-server/<int:pk>/update/', GameServerUpdateView.as_view(), name='gameserver_update'),
    path('game-server/<int:pk>/delete/', GameServerDeleteView.as_view(), name='gameserver_delete'),
    path('game-server/<int:pk>/rcon', GameServerDetailRconQueryView.as_view(), name='gameserver_rcon'),
]

team_urlpatterns = [
    path('team/', RedirectView.as_view(pattern_name='team_list'), name='team_index'),
    path('team/list/', TeamListView.as_view(), name='team_list'),
    path('team/create/', TeamCreateView.as_view(), name='team_create'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('team/<int:pk>/update/', TeamUpdateView.as_view(), name='team_update'),
    path('team/<int:pk>/delete/', TeamDeleteView.as_view(), name='team_delete'),
]

match_urlpatterns = [
    path('match/', RedirectView.as_view(pattern_name='match_list'), name='match_index'),
    path('match/list/', MatchListView.as_view(), name='match_list'),
    path('match/create/', MatchCreateView.as_view(), name='match_create'),
    path('match/<int:pk>/', MatchDetailView.as_view(), name='match_detail'),
    path('match/<int:pk>/update/', MatchUpdateView.as_view(), name='match_update'),
    path('match/<int:pk>/delete/', MatchDeleteView.as_view(), name='match_delete'),
]

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='gameserver_list'), name='index'),
]
urlpatterns += gameserver_urlpatterns
urlpatterns += team_urlpatterns
urlpatterns += match_urlpatterns