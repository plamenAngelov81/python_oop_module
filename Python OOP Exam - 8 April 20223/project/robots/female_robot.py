from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    BASE_FEMALE_BOT_WEIGHT = 7
    FEMALE_BOT_EAT = 1

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, weight=self.BASE_FEMALE_BOT_WEIGHT)

    def eating(self):
        self.weight += self.FEMALE_BOT_EAT
