from core.models import Team
from core.services.steam_get_player_summary_service import SteamGetPlayerSummaryService
from django.views.generic import ListView


class TeamListView(ListView):
    model = Team
    template_name = "team/team_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_players = []
        for team in context["team_list"]:
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

        all_players_with_summary = SteamGetPlayerSummaryService.execute(
            {"steam_ids": all_players}
        )

        for team in context["team_list"]:
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

        for team in context["team_list"]:
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

        return context
