from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    EQUIPMENT_TYPE = 'ElbowPad'

    def __init__(self):
        super().__init__(protection=90, price=25.0)

    def increase_price(self):
        self.price += self.price * 0.10

