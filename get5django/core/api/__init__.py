import socket

import requests
from core.models import GameServer, Match
from core.services.a2s_info_service import A2sInfoService
from core.services.rcon_service import RconService
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from nslookup import Nslookup

api = NinjaAPI()


@api.get("/nslookup")
def nslookup(request, domain: str):
    dns_query = Nslookup(dns_servers=["10.13.37.1", "9.9.9.9", "1.1.1.1", "8.8.8.8"])
    ips_record = dns_query.dns_lookup(domain)
    return ips_record.answer[0]


@api.get("/get-host-by-name")
def get_host_by_name(request, name: str):
    return socket.gethostbyname(name)


@api.get("/get-servers-at-address")
def get_servers_at_address(request, address: str):
    url = f"http://api.steampowered.com/ISteamApps/GetServersAtAddress/v0001?addr={address}"
    r = requests.get(url)
    return r.json()


@api.get("/get-server-info")
def get_server_info(request, address: str):
    print(f"address: {address}")
    info = A2sInfoService.execute({"address": address})
    print(info)
    return info


@api.post("/gameserver/{gameserver_id}/rcon")
def post_rcon(request, gameserver_id: int, command: str):
    gameserver = GameServer.objects.get(id=gameserver_id)
    return RconService.execute({"gameserver": gameserver, "command": command})


@api.get("/get5/match/{match_id}/match_config.json")
def get5_match(request, match_id: int):
    match = get_object_or_404(Match, id=match_id)

    team1_players = []
    if match.team1.player1 is not None:
        team1_players.append(match.team1.player1)
    if match.team1.player1 is not None:
        team1_players.append(match.team1.player2)
    if match.team1.player1 is not None:
        team1_players.append(match.team1.player3)
    if match.team1.player1 is not None:
        team1_players.append(match.team1.player4)
    if match.team1.player1 is not None:
        team1_players.append(match.team1.player5)

    team2_players = []
    if match.team2.player1 is not None:
        team2_players.append(match.team1.player1)
    if match.team2.player1 is not None:
        team2_players.append(match.team1.player2)
    if match.team2.player1 is not None:
        team2_players.append(match.team1.player3)
    if match.team2.player1 is not None:
        team2_players.append(match.team1.player4)
    if match.team2.player1 is not None:
        team2_players.append(match.team1.player5)

    response = {
        # "match_title": "Astralis vs. NaVi",
        # "matchid": "3123",
        "clinch_series": True,
        "num_maps": match.num_maps,
        "players_per_team": match.players_per_team,
        "coaches_per_team": 2,
        # "coaches_must_ready": true,
        # "min_players_to_ready": 2,
        # "min_spectators_to_ready": 0,
        "skip_veto": match.skip_veto,
        "veto_first": "team1",
        "side_type": "standard",
        "spectators": {
            "name": "GP Esports",
            "players": {"76561197987511774": "Anders Blume"},
        },
        "maplist": match.maplist.split("\r\n"),
        # "map_sides": [
        #     "team1_ct",
        #     "team2_ct",
        #     "knife"
        # ],
        "team1": {
            "name": match.team1.name,
            "tag": match.team1.tag,
            "flag": "NO",
            "logo": "astr",
            "players": [
                match.team1.player1,
                match.team1.player2,
            ]
            # "coaches": {
            # "76561197987144812": "Trace"
            # }
        },
        "team2": {
            "name": match.team2.name,
            "tag": match.team2.tag,
            "flag": "NO",
            "logo": "astr",
            "players": [
                match.team2.player1,
                match.team2.player2,
            ],
        },
        # "cvars": {
        #     "hostname": "Get5 Match #3123",
        #     "mp_friendly_fire": "0",
        #     "get5_stop_command_enabled": "0",
        #     "sm_practicemode_can_be_started": "0"
        # }
    }

    return response
