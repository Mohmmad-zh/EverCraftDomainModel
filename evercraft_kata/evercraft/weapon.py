class Weapon:
    def __init__(self, name, damage, attack_bonus=0, damage_bonus=0, critical_multiplier=2):
        self.name = name
        self.damage = damage
        self.attack_bonus = attack_bonus
        self.damage_bonus = damage_bonus
        self.critical_multiplier = critical_multiplier

class Longsword(Weapon):
    def __init__(self):
        super().__init__(name="Longsword", damage=5)
