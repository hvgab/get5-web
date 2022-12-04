from core.models import Match
from django import forms


class MatchCreateForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = [
            "team1",
            "team2",
            "series_type",
            "maplist",
        ]
