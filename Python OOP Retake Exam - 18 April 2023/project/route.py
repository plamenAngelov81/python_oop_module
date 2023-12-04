from project.validators import Validator


class Route:
    START_POINT_ERROR_MESSAGE = "Start point cannot be empty!"
    END_POINT_ERROR_MESSAGE = "End point cannot be empty!"
    ROUTE_LENGTH_ERROR_MESSAGE = "Length cannot be less than 1.00 kilometer!"

    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked = False

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self, value):
        Validator.check_for_empty_strings(value, self.START_POINT_ERROR_MESSAGE)
        self.__start_point = value

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, value):
        Validator.check_for_empty_strings(value, self.END_POINT_ERROR_MESSAGE)
        self.__end_point = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        Validator.check_route_length(value, self.ROUTE_LENGTH_ERROR_MESSAGE)
        self.__length = value
# class Route:
#     MIN_LENGTH = 1.00
#
#     def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
#         self.start_point = start_point
#         self.end_point = end_point
#         self.length = length
#         self.route_id = route_id
#         self.is_locked = False
#
#     @property
#     def start_point(self):
#         return self.__start_point
#
#     @start_point.setter
#     def start_point(self, value):
#         if not value.strip():
#             raise ValueError("Start point cannot be empty!")
#         self.__start_point = value
#
#     @property
#     def end_point(self):
#         return self.__end_point
#
#     @end_point.setter
#     def end_point(self, value):
#         if not value.strip():
#             raise ValueError("End point cannot be empty!")
#         self.__end_point = value
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         if value < self.MIN_LENGTH:
#             raise ValueError(f"Length cannot be less than {self.MIN_LENGTH:.2f} kilometer!")
#         self.__length = value
#
#     # def change_status(self):
#     #     self.is_locked = not self.is_locked
