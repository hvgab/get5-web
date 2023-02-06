import json
import logging

from core.models import Match
from core.services.rcon_service import RconService
from core.services.steam_get_player_summary_service import SteamGetPlayerSummaryService
from django.conf import settings
from django.views.generic import DetailView

logger = logging.getLogger(__name__)


class MatchDetailView(DetailView):
    model = Match
    template_name = "match/match_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ### Get5 Web Available ###
        if context["match"].game_server is not None:
            get5_web_available_response = RconService.execute(
                {
                    "gameserver": context["match"].game_server,
                    "command": "get5_web_available",
                }
            )

            logger.info("get5_web_available_response")
            logger.info(get5_web_available_response)
            rj, log = get5_web_available_response.split("L")

            logger.debug("rj")
            logger.debug(rj)

            logger.debug("log")
            logger.debug(log)

            response = None
            error = None
            if rj.startswith("Unknown command"):
                error = rj
            else:
                response = rj

            if response is not None:
                response = json.loads(response)

            context["get5_web_available"] = {
                "full": get5_web_available_response,
                "response": response,
                "log": log,
                "error": error,
            }

        ### Match Teams With Steam Data ###
        team_list = [context["match"].team1, context["match"].team2]
        all_players = []
        for team in team_list:
            if team.player1 is not None:
                all_players.append(team.player1)
            if team.player2 is not None:
                all_players.append(team.player2)
            if team.player3 is not None:
                all_players.append(team.player3)
            if team.player4 is not None:
                all_players.append(team.player4)
            if team.player5 is not None:
                all_players.append(team.player5)

        if all_players:
            all_players_with_summary = SteamGetPlayerSummaryService.execute(
                {"steam_ids": all_players}
            )

        for team in team_list:
            for player_summary in all_players_with_summary:
                if team.player1 == player_summary["steamid"]:
                    team.player1 = player_summary
                if team.player2 == player_summary["steamid"]:
                    team.player2 = player_summary
                if team.player3 == player_summary["steamid"]:
                    team.player3 = player_summary
                if team.player4 == player_summary["steamid"]:
                    team.player4 = player_summary
                if team.player5 == player_summary["steamid"]:
                    team.player5 = player_summary

        for team in team_list:
            if isinstance(team.player1, str):
                team.player1 = {"personaname": team.player1}
            if isinstance(team.player2, str):
                team.player2 = {"personaname": team.player2}
            if isinstance(team.player3, str):
                team.player3 = {"personaname": team.player3}
            if isinstance(team.player4, str):
                team.player4 = {"personaname": team.player4}
            if isinstance(team.player5, str):
                team.player5 = {"personaname": team.player5}

        context["match"].team1, context["match"].team2 = team_list

        context["GET5_API_HOST"] = settings.GET5_API_HOST

        return context
