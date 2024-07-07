class Item:
    def __init__(self, name):
        self.name = name

class RingOfProtection(Item):
    def __init__(self):
        super().__init__(name="Ring of Protection")
        self.armor_class_bonus = 2

class BeltOfGiantStrength(Item):
    def __init__(self):
        super().__init__(name="Belt of Giant Strength")
        self.strength_bonus = 4
