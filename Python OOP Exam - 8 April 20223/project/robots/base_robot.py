from abc import ABC, abstractmethod

from project.validators import Validator


class BaseRobot(ABC):
    ROBOT_NAME_ERROR_MESSAGE = "Robot name cannot be empty!"
    ROBOT_KIND_ERROR_MESSAGE = "Robot kind cannot be empty!"
    ROBOT_PRICE_ERROR_MESSAGE = "Robot price cannot be less than or equal to 0.0!"

    def __init__(self, name, kind, price, weight):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_strings(value, self.ROBOT_NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        Validator.check_for_empty_strings(value, self.ROBOT_KIND_ERROR_MESSAGE)
        self.__kind = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.price_check(value, self.ROBOT_PRICE_ERROR_MESSAGE)
        self.__price = value

    @abstractmethod
    def eating(self):
        pass
