from abc import ABC, abstractmethod

from project.validators import Validator


class BaseService(ABC):
    SERVICE_NAME_ERROR_MESSAGE = "Service name cannot be empty!"
    SERVICE_CAPACITY_ERROR_MESSAGE = "Service capacity cannot be less than or equal to 0!"

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError(self.SERVICE_NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError(self.SERVICE_CAPACITY_ERROR_MESSAGE)
        self.__capacity = value

    @abstractmethod
    def details(self):
        pass
