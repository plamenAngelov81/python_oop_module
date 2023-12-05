from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    BASE_MALE_BOT_WEIGHT = 9
    MALE_BOT_EAT = 3

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, weight=self.BASE_MALE_BOT_WEIGHT)

    def eating(self):
        self.weight += self.MALE_BOT_EAT
