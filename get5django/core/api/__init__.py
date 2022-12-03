
from ninja import NinjaAPI
import socket
import requests
from nslookup import Nslookup
from core.services.a2s_info_service import A2sInfoService
from core.models import GameServer
from core.services.rcon_service import RconService
api = NinjaAPI()

@api.get("/nslookup")
def nslookup(request, domain:str):
    dns_query = Nslookup(dns_servers=["10.13.37.1","9.9.9.9","1.1.1.1","8.8.8.8"])
    ips_record = dns_query.dns_lookup(domain)
    return ips_record.answer[0]

@api.get("/get-host-by-name")
def get_host_by_name(request, name:str):
    return socket.gethostbyname(name)

@api.get('/get-servers-at-address')
def get_servers_at_address(request, address:str):
    url = f'http://api.steampowered.com/ISteamApps/GetServersAtAddress/v0001?addr={address}'
    r = requests.get(url)
    return r.json()

@api.get('/get-server-info')
def get_server_info(request, address:str):
    print(f"address: {address}")
    info = A2sInfoService.execute({'address':address})
    print(info)
    return info

@api.post('/gameserver/{gameserver_id}/rcon')
def post_rcon(request, gameserver_id:int, command:str):
    gameserver = GameServer.objects.get(id=gameserver_id)
    return RconService.execute({'gameserver':gameserver, 'command':command})