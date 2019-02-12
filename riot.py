import datetime
from typing import List


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


class SummonerStats:
    def __init__(
            self,
            summoner: SummonerDTO,
            support: bool,
            first_game: bool,
            honored: bool,
            match_points: int
    ):
        self.summoner = summoner
        self.support = support
        self.first_game = first_game
        self.honored = honored
        self.match_points = match_points

        super().__init__()


class Match:
    def __init__(
            self,
            time: datetime,
            players: List[SummonerDTO],

    ):
        self.time = time
        self.players = players

    super().__init__()
