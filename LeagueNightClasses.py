import datetime
from typing import List


# Riot's Summoner Class
class SummonerDTO:
    def __init__(
            self,
            profileIconId: int,
            name: str,
            puuid: str,
            summonerLevel: int,
            revisionDate: int,
            id: int,
            accountId: int
    ):
        self.profileIconId = profileIconId
        self.name = name
        self.puuid = puuid
        self.summonerLevel = summonerLevel
        self.revisionDate = revisionDate
        # self.id = id
        self.accountId = accountId
        self.points = 3

        super().__init__()


# A class to track a summoner's stats per game
class SummonerStats:
    def __init__(
            self,
            summoner: SummonerDTO,
            support: bool,
            first_game: bool,
            honored: bool,
            match_points: int,
            team: int
    ):
        self.summoner = summoner
        self.support = support
        self.first_game = first_game
        self.honored = honored
        self.match_points = match_points
        self.team = team

        super().__init__()


# A class to record a match's results
class Match:
    def __init__(
            self,
            time: datetime,
            players: List[SummonerStats],

    ):
        self.time = time
        self.players = players

        super().__init__()
