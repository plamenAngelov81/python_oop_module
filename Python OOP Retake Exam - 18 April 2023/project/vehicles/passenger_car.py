from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.0
    VEHICLE_TYPE = 'PassengerCar'

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        consumed_battery = (mileage / self.MAX_MILEAGE) * 100
        self.battery_level -= round(consumed_battery)
