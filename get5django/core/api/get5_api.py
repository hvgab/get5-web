
from datetime import date
from ninja import Schema
from core.models import Match
from django.shortcuts import get_object_or_404


class MatchGet5Out(Schema):
    match_title: str | None
    matchid: str | None
    clinch_series: bool | None
    num_maps: int | None
    players_per_team: int | None
    coaches_per_team: int | None
    coaches_must_ready: bool | None
    min_players_to_ready: int | None
    min_spectators_to_ready: int | None
    skip_veto: bool | None
    veto_first: "team1" | "team2" | "random" | None
    side_type: "standard" | "always_knife" | "never_knife" | None
    map_sides: ["team1_ct" | "team1_t" | "knife"] | None
    spectators: {
        name: str | None
        players: Get5PlayerSet | None
    } | None,
    maplist: [str]
    favored_percentage_team1: int | None
    favored_percentage_text: str | None
    team1: Get5MatchTeam | Get5MatchTeamFromFile
    team2: Get5MatchTeam | Get5MatchTeamFromFile
    # "cvars": { [key: str]: str | int } | None

@api.get("/get5/match/{match_id}")
def get5_match(request, match_id:int):
    match = get_object_or_404(Match, id=match_id)
    
    response = {
        # "match_title": "Astralis vs. NaVi",
        # "matchid": "3123",
        "clinch_series": True,
        "num_maps": 3,
        "players_per_team": 2,
        "coaches_per_team": 2,
        # "coaches_must_ready": true,
        # "min_players_to_ready": 2,
        # "min_spectators_to_ready": 0,
        "skip_veto": False,
        "veto_first": "team1",
        "side_type": "standard",
        "spectators": {
            "name": "GP Esports",
            "players": {
            "76561197987511774": "Anders Blume"
            }
        },
        "maplist": [
            "de_dust2",
            "de_nuke",
            "de_inferno",
            "de_mirage",
            "de_vertigo",
            "de_ancient",
            "de_overpass"
        ],
        # "map_sides": [
        #     "team1_ct",
        #     "team2_ct",
        #     "knife"
        # ],
        "team2": {
            "name": "Astralis",
            "tag": "Astralis",
            "flag": "DK",
            "logo": "astr",
            "players": {
                # "76561197990682262": "Xyp9x",
                # "76561198010511021": "gla1ve",
                # "76561197979669175": "K0nfig",
                # "76561198028458803": "BlameF",
                # "76561198024248129": "farlig"
            },
            # "coaches": {
                # "76561197987144812": "Trace"
            # }
        },
        "team2": {
            "name": "Astralis",
            "tag": "Astralis",
            "flag": "DK",
            "logo": "astr",
            "players": {
                "76561197990682262": "Xyp9x",
                "76561198010511021": "gla1ve",
                "76561197979669175": "K0nfig",
                "76561198028458803": "BlameF",
                "76561198024248129": "farlig"
            },
            "coaches": {
                "76561197987144812": "Trace"
            }
        },
        # "cvars": {
        #     "hostname": "Get5 Match #3123",
        #     "mp_friendly_fire": "0",
        #     "get5_stop_command_enabled": "0",
        #     "sm_practicemode_can_be_started": "0"
        # }
    }

    return response