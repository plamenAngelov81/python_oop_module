from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    FISH_TYPE = 'PredatoryFish'
    TIME_TO_CATCH = 90

    def __init__(self, name, points):
        super().__init__(name, points, self.TIME_TO_CATCH)

    def fish_details(self):
        return f"{self.FISH_TYPE}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"
