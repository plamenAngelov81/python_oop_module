from abc import ABC, abstractmethod
from project.validators import Validator
from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    DIVER_NAME_ERROR_MESSAGE = "Diver name cannot be null or empty!"
    NEGATIVE_OXYGEN_LEVEL_MESSAGE = "Cannot create diver with negative oxygen level!"

    def __init__(self, name, oxygen_level):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0.0
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_string(value, self.DIVER_NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        Validator.check_oxygen_level(value, self.NEGATIVE_OXYGEN_LEVEL_MESSAGE)
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def hit(self, fish: BaseFish):
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points += round(fish.points, 1)
