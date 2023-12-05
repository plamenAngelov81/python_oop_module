from project.services.base_service import BaseService


class MainService(BaseService):
    MAIN_SERVICE_CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, capacity=self.MAIN_SERVICE_CAPACITY)

    def details(self):
        result = f"{self.name} Main Service:\n"
        if len(self.robots) == 0:
            result += "Robots: none"
        else:
            current_robots = []
            for robot in self.robots:
                current_robots.append(robot.name)
            result += f"Robots: {' '.join(current_robots)}"

        return result
