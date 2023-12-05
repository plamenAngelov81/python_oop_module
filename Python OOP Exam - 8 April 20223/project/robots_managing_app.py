from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    VALID_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def get_robot(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot
        return None

    def get_service(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service
        return None

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")
        new_service = self.VALID_SERVICES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")
        new_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        compatibility_dict = {
            'MaleRobot': 'MainService',
            'FemaleRobot': 'SecondaryService'
        }
        current_robot = self.get_robot(robot_name)
        current_service = self.get_service(service_name)

        robot_class_type = current_robot.__class__.__name__
        service_class_type = current_service.__class__.__name__
        if compatibility_dict[robot_class_type] != service_class_type:
            return "Unsuitable service."

        if len(current_service.robots) >= current_service.capacity:
            raise Exception("Not enough capacity for this robot!")

        current_service.robots.append(current_robot)
        self.robots.remove(current_robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        current_service = self.get_service(service_name)
        robots = [robot for robot in current_service.robots if robot.name == robot_name]
        if len(robots) == 0:
            raise Exception("No such robot in this service!")

        current_robot = robots[0]
        current_service.robots.remove(current_robot)
        self.robots.append(current_robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        current_service = self.get_service(service_name)
        for robot in current_service.robots:
            robot.eating()
        return f"Robots fed: {len(current_service.robots)}."

    def service_price(self, service_name: str):
        current_service = self.get_service(service_name)
        total_price = sum([robot.price for robot in current_service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join([service.details() for service in self.services])

# class RobotsManagingApp:
#     SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
#     ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
#
#     ERROR_MSG_TYPE_SERVICE = "Invalid service type!"
#     ERROR_MSG_TYPE_ROBOT = "Invalid robot type!"
#     ERROR_MSG_CAPACITY = "Not enough capacity for this robot!"
#     ERROR_MSG_NO_ROBOT = "No such robot in this service!"
#
#     def __init__(self):
#         self.robots = []
#         self.services = []
#
#     def add_service(self, service_type: str, name: str):
#         self._check_service_type(service_type)
#         new_service_obj = self._create_service(service_type, name)
#         self.services.append(new_service_obj)
#         return f"{service_type} is successfully added."
#
#     def add_robot(self, robot_type: str, name: str, kind: str, price: float):
#         self._check_robot_type(robot_type)
#         new_robot_obj = self._create_robot(robot_type, name, kind, price)
#         self.robots.append(new_robot_obj)
#         return f"{robot_type} is successfully added."
#
#     def add_robot_to_service(self, robot_name: str, service_name: str):
#         robot_obj = self._find_obj_by_name(robot_name, self.robots)
#         service_obj = self._find_obj_by_name(service_name, self.services)
#         if robot_obj.POSSIBLE_SERVICE != service_obj.__class__.__name__:
#             return "Unsuitable service."
#         if len(service_obj.robots) >= service_obj.capacity:
#             raise Exception(self.ERROR_MSG_CAPACITY)
#         self.robots.remove(robot_obj)
#         service_obj.robots.append(robot_obj)
#         return f"Successfully added {robot_name} to {service_name}."
#
#     def remove_robot_from_service(self, robot_name: str, service_name: str):
#         service_obj = self._find_obj_by_name(service_name, self.services)
#         robot = [r for r in service_obj.robots if r.name == robot_name]
#         if not robot:
#             raise Exception(self.ERROR_MSG_NO_ROBOT)
#         robot_obj = robot[0]
#         service_obj.robots.remove(robot_obj)
#         self.robots.append(robot_obj)
#         return f"Successfully removed {robot_name} from {service_name}."
#
#     def feed_all_robots_from_service(self, service_name: str):
#         service_obj = self._find_obj_by_name(service_name, self.services)
#         [r.eating() for r in service_obj.robots]
#         return f"Robots fed: {len(service_obj.robots)}."
#
#     def service_price(self, service_name: str):
#         service_obj = self._find_obj_by_name(service_name, self.services)
#         total_price = sum([r.price for r in service_obj.robots])
#         return f"The value of service {service_name} is {total_price:.2f}."
#
#     def __str__(self):
#         return '\n'.join([s.details() for s in self.services])
#
#     def _check_service_type(self, service_type):
#         if service_type not in self.SERVICE_TYPES:
#             raise Exception(self.ERROR_MSG_TYPE_SERVICE)
#
#     def _check_robot_type(self, robot_type):
#         if robot_type not in self.ROBOT_TYPES:
#             raise Exception(self.ERROR_MSG_TYPE_ROBOT)
#
#     def _create_service(self, service_type, name):
#         return self.SERVICE_TYPES[service_type](name)
#
#     def _create_robot(self, robot_type, name, kind, price):
#         return self.ROBOT_TYPES[robot_type](name, kind, price)
#
#     @staticmethod
#     def _find_obj_by_name(name, collection):
#         return [obj for obj in collection if obj.name == name][0]
