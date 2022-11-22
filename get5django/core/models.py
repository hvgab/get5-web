from django.db import models
from core.services.a2s_info_service import A2sInfoService

# Create your models here.
class GameServer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)

    url = models.CharField(max_length=255)
    port = models.IntegerField()
    
    ssh_user = models.CharField(max_length=255, null=True, blank=True)
    ssh_password = models.CharField(max_length=255, null=True, blank=True)
    
    
    player_password = models.CharField(max_length=255, null=True, blank=True)
    rcon_password = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_info(self):
        return A2sInfoService.execute({'address':f'{self.url}:{self.port}'})

class Team(models.Model):
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=40, default='')
    flag = models.CharField(max_length=4, default='')
    logo = models.CharField(max_length=10, default='')

class Match(models.Model):
    game_server = models.ForeignKey('GameServer', on_delete=models.CASCADE)
    team1 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='match_set_as_team1')
    team2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='match_set_as_team2')
    winner = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='match_set_as_team_winner')
    plugin_version = models.CharField(max_length=32, default='unknown')

    forfeit = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_maps = models.IntegerField()
    title = models.CharField(max_length=60, default='')
    skip_veto = models.BooleanField()
    api_key = models.CharField(max_length=32)

    veto_mappool = models.CharField(max_length=500)
    # map_stats

    team1_score = models.IntegerField()
    team2_score = models.IntegerField()

    @property
    def finalized(self):
        return self.cancelled or self.finished

    @property
    def is_pending(self):
        return self.start_time is None and not self.cancelled

    @property
    def is_finished(self):
        return self.end_time is not None and not self.cancelled

    @property
    def is_live(self):
        return self.start_time is not None and self.end_time is None and not self.cancelled

class Player(models.Model):
    steam_id = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    



