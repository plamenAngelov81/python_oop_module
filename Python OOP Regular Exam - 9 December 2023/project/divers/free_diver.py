from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    DIVER_TYPE = 'FreeDiver'
    DIVER_OXYGEN_LEVEL = 120

    def __init__(self, name):
        super().__init__(name, self.DIVER_OXYGEN_LEVEL)

    def renew_oxy(self):
        self.oxygen_level = self.DIVER_OXYGEN_LEVEL

    def miss(self, time_to_catch):
        needed_oxygen = round(time_to_catch * 0.6)
        if self.oxygen_level < needed_oxygen:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= needed_oxygen

    def __str__(self):
        return f"{self.DIVER_TYPE}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, " \
               f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"
