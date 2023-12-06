from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def get_equipment_by_type(self, equipment_type):
        stuff = [st for st in self.equipment if st.EQUIPMENT_TYPE == equipment_type]
        return stuff

    def get_team_by_name(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team
        return None

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        new_equipment = self.EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self.get_team_by_name(team_name)
        equipment = self.get_equipment_by_type(equipment_type)[-1]
        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.get_team_by_name(team_name)
        if team is None:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        filtered_equipments = self.get_equipment_by_type(equipment_type)
        [equipment.increase_price() for equipment in filtered_equipments]
        return f"Successfully changed {len(filtered_equipments)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_one = self.get_team_by_name(team_name1)
        team_two = self.get_team_by_name(team_name2)

        if team_one.TEAM_TYPE != team_two.TEAM_TYPE:
            raise Exception("Game cannot start! Team types mismatch!")

        team_one_points = team_one.advantage + sum(item.protection for item in team_one.equipment)
        team_two_points = team_two.advantage + sum(item.protection for item in team_two.equipment)

        if team_one_points > team_two_points:
            team_one.win()
            return f"The winner is {team_one.name}."
        elif team_two_points > team_one_points:
            team_two.win()
            return f"The winner is {team_two.name}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:"""]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)
