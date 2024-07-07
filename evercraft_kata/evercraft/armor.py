class Armor:
    def __init__(self, name, armor_class_bonus):
        self.name = name
        self.armor_class_bonus = armor_class_bonus

class LeatherArmor(Armor):
    def __init__(self):
        super().__init__(name="Leather Armor", armor_class_bonus=2)
