from django import forms
from core.models import Match

class MatchCreateForm(forms.ModelForm):
    class Meta:
        model=Match
        fields = [
            'team1',
            'team2',
            'series_type',
            'veto_mappool',
        ]