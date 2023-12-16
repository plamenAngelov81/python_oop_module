from abc import ABC, abstractmethod
from project.validators import Validator


class BaseFish(ABC):
    NAME_ERROR_MESSAGE = "Fish name should be determined!"
    POINTS_ERROR_MESSAGE = "Points should be a value ranging from 1 to 10!"

    def __init__(self, name, points, time_to_catch):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_string(value, self.NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        Validator.check_points(value, self.POINTS_ERROR_MESSAGE)
        self.__points = value

    @abstractmethod
    def fish_details(self):
        pass
