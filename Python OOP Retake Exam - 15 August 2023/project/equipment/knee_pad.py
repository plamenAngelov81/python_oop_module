from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    EQUIPMENT_TYPE = 'KneePad'

    def __init__(self):
        super().__init__(protection=120, price=15.0)

    def increase_price(self):
        self.price += self.price * 0.2
