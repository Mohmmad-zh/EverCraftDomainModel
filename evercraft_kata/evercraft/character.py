# character.py

from .abilities import Abilities
from .experience import Experience
from .level import Level
from .class_ import Fighter, Rogue

class Character:
    def __init__(self, name, alignment):
        self.name = name
        self.alignment = alignment
        self.armor_class = 10
        self.hit_points = 5
        self.abilities = Abilities()
        self.experience = Experience()
        self.level = Level()
        self.attack_bonus = 0  # Initialize attack bonus

    def apply_class_bonuses(self, character_class):
        if character_class == "Fighter":
            Fighter.apply_class_bonuses(self)
        elif character_class == "Rogue":
            Rogue.apply_class_bonuses(self)

    def calculate_armor_class(self):
        return self.armor_class + self.abilities.dexterity_modifier

    def attack(self, opponent, roll):
        if roll == 20:
            damage = 2 * self.abilities.strength_modifier
        else:
            damage = max(1, self.abilities.strength_modifier)

        if roll >= opponent.calculate_armor_class():
            if roll == 20:
                damage *= 2
            opponent.take_damage(damage)
            self.gain_experience(10)
            return True  # Indicate successful attack
        else:
            return False  # Indicate unsuccessful attack

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.hit_points = 0  # Ensure hit points do not go negative
            # Additional logic for handling character death or status change

    def gain_experience(self, points):
        self.experience.points += points

    def level_up(self):
        self.level.increase()
        self.hit_points += self.level.calculate_hit_points(self.abilities.constitution_modifier)
        if self.level.level % 2 == 0:
            self.attack_bonus += 1
