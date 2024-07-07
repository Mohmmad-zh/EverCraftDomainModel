class Class:
       def apply_class_bonuses(self, character_class):
        if character_class == "Fighter":
            self.attack_bonus += self.abilities.strength_modifier
        elif character_class == "Rogue":
            self.attack_bonus += self.abilities.dexterity_modifier
# class_.py

class Fighter:
    @staticmethod
    def apply_class_bonuses(character):
        character.hit_points += 10 + character.abilities.constitution_modifier
        character.attack_bonus += 1

class Rogue:
    @staticmethod
    def apply_class_bonuses(character):
        character.attack_bonus += character.abilities.dexterity_modifier


class Monk(Class):
    def apply_class_bonuses(self, character):
        character.hit_points += 5 * (character.level - 1)
        character.armor_class += character.abilities.wisdom_modifier

class Paladin(Class):
    def apply_class_bonuses(self, character):
        character.hit_points += 8 * (character.level - 1)
