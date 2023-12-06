from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    TEAM_TYPE = 'OutdoorTeam'

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=1000)

    def win(self):
        self.advantage += 115
        self.wins += 1
