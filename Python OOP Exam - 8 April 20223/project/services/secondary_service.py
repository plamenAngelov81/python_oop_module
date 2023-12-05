from project.services.base_service import BaseService


class SecondaryService(BaseService):
    SECONDARY_SERVICE_CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, self.SECONDARY_SERVICE_CAPACITY)

    def details(self):
        result = f"{self.name} Secondary Service:\n"
        if len(self.robots) == 0:
            result += "Robots: none"
        else:
            current_robots = []
            for robot in self.robots:
                current_robots.append(robot.name)
            result += f"Robots: {' '.join(current_robots)}"

        return result
