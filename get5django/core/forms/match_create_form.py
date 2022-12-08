from core.models import Match
from django import forms


class MatchCreateForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = [
            "game_server",
            "match_title",
            "match_date_time",
            "team1",
            "team2",
            "num_maps",
            "players_per_team",
            "maplist",
        ]
        widgets = {
            "match_date_time": forms.DateTimeInput({"type": "datetime-local"}),
        }
