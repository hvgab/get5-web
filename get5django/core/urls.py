from core.views import GameServerDeleteView
from core.views import GameServerUpdateView
from core.views import GameServerDetailView
from core.views import GameServerCreateView
from core.views import GameServerListView

from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
path('game_server/list/', GameServerListView.as_view(), name='game_server_list'),
path('game_server/create/', GameServerCreateView.as_view(), name='game_server_create'),
path('game_server/detail/<int:pk>/', GameServerDetailView.as_view(), name='game_server_detail'),
path('game_server/update/<int:pk>/', GameServerUpdateView.as_view(), name='game_server_update'),
path('game_server/delete/<int:pk>/', GameServerDeleteView.as_view(), name='game_server_delete'),
    ]
