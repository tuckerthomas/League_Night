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
