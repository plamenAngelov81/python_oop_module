from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    FISH_TYPE = 'DeepSeaFish'
    TIME_TO_CATCH = 180

    def __init__(self, name, points):
        super().__init__(name, points, self.TIME_TO_CATCH)

    def fish_details(self):
        return f"{self.FISH_TYPE}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"
