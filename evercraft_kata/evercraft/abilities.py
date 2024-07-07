class Abilities:
    def __init__(self, strength=10, dexterity=10, constitution=10, wisdom=10, intelligence=10, charisma=10):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @staticmethod
    def calculate_modifier(score):
        return (score - 10) // 2

    @property
    def strength_modifier(self):
        return self.calculate_modifier(self.strength)

    @property
    def dexterity_modifier(self):
        return self.calculate_modifier(self.dexterity)

    @property
    def constitution_modifier(self):
        return self.calculate_modifier(self.constitution)

    @property
    def wisdom_modifier(self):
        return self.calculate_modifier(self.wisdom)

    @property
    def intelligence_modifier(self):
        return self.calculate_modifier(self.intelligence)

    @property
    def charisma_modifier(self):
        return self.calculate_modifier(self.charisma)
