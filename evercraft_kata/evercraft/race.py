class Race:
    def apply_modifiers(self, character):
        pass

class Human(Race):
    pass

class Orc(Race):
    def apply_modifiers(self, character):
        character.abilities.strength += 2
        character.abilities.intelligence -= 1
        character.abilities.wisdom -= 1
        character.abilities.charisma -= 1
        character.armor_class += 2

class Dwarf(Race):
    def apply_modifiers(self, character):
        character.abilities.constitution += 1
        character.abilities.charisma -= 1

class Elf(Race):
    def apply_modifiers(self, character):
        character.abilities.dexterity += 1
        character.abilities.constitution -= 1

class Halfling(Race):
    def apply_modifiers(self, character):
        character.abilities.dexterity += 1
        character.abilities.strength -= 1
