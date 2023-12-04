from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLES = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def _find_driver_by_driving_license(self, driving_license):
        for driver in self.users:
            if driver.driving_license_number == driving_license:
                return driver
        return None

    def _get_vehicle_by_pate_number(self, pate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == pate_number:
                return vehicle
        return None

    def _find_route_by_start_end_point(self, start_point: str, end_point: str):
        routes = [route for route in self.routes
                  if route.start_point == start_point and route.end_point == end_point]
        if routes:
            return routes[0]
        return None

    def _find_route_by_id(self, route_id):
        for route in self.routes:
            if route.route_id == route_id:
                return route
        return None

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self._find_driver_by_driving_license(driving_license_number)
        if user:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        vehicle = self._get_vehicle_by_pate_number(license_plate_number)
        if vehicle_type not in self.VALID_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VALID_VEHICLES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = self._find_route_by_start_end_point(start_point, end_point)

        if route is not None:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.length > length:
                route.is_locked = True

        current_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id=current_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self._find_driver_by_driving_license(driving_license_number)
        vehicle = self._get_vehicle_by_pate_number(license_plate_number)
        route = self._find_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        sorted_cars = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))[:count]

        for vehicle in sorted_cars:
            vehicle.is_damaged = False
            vehicle.battery_level = 100
        return f"{len(sorted_cars)} vehicles were successfully repaired!"

    def users_report(self):
        users = sorted(self.users, key=lambda x: -x.rating)
        result = ["*** E-Drive-Rent ***"]
        for user in users:
            result.append(str(user))

        return '\n'.join(result)
