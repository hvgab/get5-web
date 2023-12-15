from django.conf import settings
from django.db import models


# Create your models here.
class GameServer(models.Model):

    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_gameservers",
    )
    admins = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="admined_gameservers"
    )

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)

    url = models.CharField(max_length=255)
    internal_url = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="If you are hosting this app on the same local network as the game-server.",
    )
    port = models.IntegerField()

    public = models.BooleanField(
        verbose_name="Is the server public?",
        name="Is Public",
    )

    ssh_user = models.CharField(max_length=255, null=True, blank=True)
    ssh_password = models.CharField(max_length=255, null=True, blank=True)

    player_password = models.CharField(max_length=255, null=True, blank=True)
    rcon_password = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    @property
    def rcon_url(self):
        if self.internal_url is not None:
            return self.internal_url
        return self.url

    def get_info(self):
        from core.services.a2s_info_service import A2sInfoService

        return A2sInfoService.execute({"gameserver": self})

    def get_players(self):
        from core.services.a2s_player_service import A2sPlayerService

        return A2sPlayerService.execute({"gameserver": self})

    def get_rules(self):
        from core.services.a2s_rules_service import A2sRulesService

        return A2sRulesService.execute({"gameserver": self})


class Player(models.Model):
    nickname = models.CharField(max_length=128)
    steam_id = models.CharField(
        max_length=128,
        unique=True,
        null=True,
        blank=True,
        help_text="SteamId i steamID64 format. (feks '76561197983132487'). Man kan konvertere steam iden sin her https://steamid.io",
    )
    # steam_data = models.TextField()
    esportal_username = models.CharField(
        max_length=128,
        unique=True,
        null=True,
        blank=True,
        help_text="Hvis dette er linken https://esportal.com/en/profile/Gabbeh/ skal det skrives inn 'Gabbeh' her.",
    )
    # esportal_data = models.TextField()


class Team(models.Model):
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=40, default="")
    flag = models.CharField(max_length=4, default="NO")
    logo = models.CharField(max_length=10, default="", null=True, blank=True)
    player1 = models.CharField(max_length=255, null=True, blank=True)
    player2 = models.CharField(max_length=255, null=True, blank=True)
    player3 = models.CharField(max_length=255, null=True, blank=True)
    player4 = models.CharField(max_length=255, null=True, blank=True)
    player5 = models.CharField(max_length=255, null=True, blank=True)
    player6 = models.CharField(max_length=255, null=True, blank=True)
    player7 = models.CharField(max_length=255, null=True, blank=True)

    # players = models.ManyToManyField(to=Player, related_name='teams', null=True, blank=True)

    def __str__(self) -> str:
        return f"[{self.tag}] {self.name}"


class Match(models.Model):
    SERIES_TYPE_CHOICES = [
        (
            "MAP PRESET",
            (("BO1_MAP_PRESET", "BO1 with map preset"),),
        ),
        (
            "MAP VETO",
            (
                ("BO1_MAP_VETO", "BO1 with map veto"),
                ("BO3_MAP_VETO", "BO3 with map veto"),
            ),
        ),
    ]

    game_server = models.ForeignKey(
        "GameServer", on_delete=models.CASCADE, null=True, blank=True
    )

    # To create a Get5 Match
    match_title = models.CharField(
        max_length=64,
        default=None,
        null=True,
        blank=True,
        help_text="La denne være blank så fikser Get5 Tittel selv.",
    )

    match_date_time = models.DateTimeField(
        null=True, blank=True, help_text="When is the match planned for?"
    )

    clinch_series = models.BooleanField(
        default=True,
        help_text="Don't play third match in BO3 if one team has already won 2.",
    )
    num_maps = models.IntegerField(default=3)
    players_per_team = models.IntegerField(default=5)
    # coaches_per_team = models.IntegerField(default=2)
    # coaches_must_ready = models.BooleanField(default=False)
    # min_players_to_ready = models.IntegerField(default=0)
    # min_spectators_to_ready = models.IntegerField(default=0)
    skip_veto = models.BooleanField(default=False)
    # veto_first = models.CharField(choices=('team1', 'team2', 'random'), default='team1')
    # side_type = models.CharField(choices=('standard', 'always_knife', 'never_knife'), default='standard')
    # map_sides =
    # spectators
    maplist = models.TextField(
        max_length=1024,
        default="""*** Competitive ***
de_inferno
de_overpass
de_train
de_vertigo
de_ancient
de_anubis
de_breach
de_cache
de_dust2
de_mirage
de_tuscan
de_nuke

*** Wingman ***
de_inferno
de_overpass
de_train
de_vertigo
de_blagai
de_cbble
de_lake
de_prime
de_shortdust
de_shortnuk

*** Wingman Workshop ***
de_marine
de_gracia
de_evon
de_eternity
de_akihabara
de_austria
de_beerhouse

*** Vintercup ***
de_inferno
de_overpass
de_train
de_vertigo
de_cbble
de_lake
de_shortdust
""",
        help_text="7 Maps. One map per line.",
    )

    team1 = models.ForeignKey(
        "Team", on_delete=models.CASCADE, related_name="match_set_as_team1"
    )
    team2 = models.ForeignKey(
        "Team", on_delete=models.CASCADE, related_name="match_set_as_team2"
    )
    series_type = models.CharField(max_length=64, choices=SERIES_TYPE_CHOICES)

    winner = models.ForeignKey(
        "Team",
        on_delete=models.CASCADE,
        related_name="match_set_as_team_winner",
        null=True,
        blank=True,
    )
    plugin_version = models.CharField(
        max_length=32, default="unknown", null=True, blank=True
    )

    forfeit = models.BooleanField(default=False, null=True, blank=True)
    cancelled = models.BooleanField(default=False, null=True, blank=True)
    finished = models.BooleanField(default=False, null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    max_maps = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=60, default="", null=True, blank=True)
    api_key = models.CharField(max_length=32, null=True, blank=True)

    veto_mappool = models.CharField(max_length=500, null=True, blank=True)
    # map_stats

    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.team1} vs {self.team2}"

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
        return (
            self.start_time is not None and self.end_time is None and not self.cancelled
        )


class Organization(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organization_set_as_owner",
    )
    admins = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="organization_set_as_admin",
        null=True,
        blank=True,
    )


class Cup(models.Model):
    name = models.CharField(max_length=64)
    organization = models.ForeignKey(
        "organization", on_delete=models.SET_NULL, null=True, blank=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cup_set_as_owner",
    )
    admins = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cup_set_as_admin", null=True, blank=True
    )
