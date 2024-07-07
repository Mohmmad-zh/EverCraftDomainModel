# EverCraft Kata

This project is a domain model for the EverCraft Kata, an exercise for building out a domain model for an MMORPG called EverCraft.

## Project Structure

The project is organized as follows:



Sure! Here's a complete Python project structure for the EverCraft Kata, covering all the specified features.

Project Structure
markdown
Copy code
evercraft_kata/
├── evercraft/
│   ├── __init__.py
│   ├── abilities.py
│   ├── alignment.py
│   ├── character.py
│   ├── combat.py
│   ├── experience.py
│   ├── level.py
│   ├── race.py
│   ├── class_.py
│   ├── weapon.py
│   ├── armor.py
│   └── item.py
├── tests/
│   ├── __init__.py
│   ├── test_abilities.py
│   ├── test_alignment.py
│   ├── test_character.py
│   ├── test_combat.py
│   ├── test_experience.py
│   ├── test_level.py
│   ├── test_race.py
│   ├── test_class_.py
│   ├── test_weapon.py
│   ├── test_armor.py
│   └── test_item.py
└── README.md
evercraft/init.py
This file can be left empty or used to initialize the package.

evercraft/abilities.py
python
Copy code
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
evercraft/alignment.py
python
Copy code
class Alignment:
    GOOD = 'Good'
    EVIL = 'Evil'
    NEUTRAL = 'Neutral'

    @staticmethod
    def is_valid(alignment):
        return alignment in [Alignment.GOOD, Alignment.EVIL, Alignment.NEUTRAL]
evercraft/character.py
python
Copy code
from .abilities import Abilities
from .alignment.py import Alignment

class Character:
    def __init__(self, name, alignment):
        self.name = name
        if not Alignment.is_valid(alignment):
            raise ValueError("Invalid alignment")
        self.alignment = alignment
        self.armor_class = 10
        self.hit_points = 5
        self.experience_points = 0
        self.level = 1
        self.abilities = Abilities()
        self.alive = True

    def calculate_armor_class(self):
        return self.armor_class + self.abilities.dexterity_modifier

    def attack(self, opponent, roll):
        attack_roll = roll + self.abilities.strength_modifier
        if roll == 20 or attack_roll >= opponent.calculate_armor_class():
            damage = 1 + self.abilities.strength_modifier
            if roll == 20:
                damage = max(2 * damage, 1)
            opponent.take_damage(damage)
            self.gain_experience(10)
            return True
        return False

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.alive = False

    def gain_experience(self, points):
        self.experience_points += points
        while self.experience_points >= self.level * 1000:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hit_points += 5 + max(self.abilities.constitution_modifier, 1)
        if self.level % 2 == 0:
            self.attack_bonus += 1
evercraft/combat.py
This module will handle the combat logic.

python
Copy code
def roll_die(sides=20):
    import random
    return random.randint(1, sides)
evercraft/experience.py
python
Copy code
class Experience:
    def __init__(self, points=0):
        self.points = points

    def add(self, points):
        self.points += points

    def level_up(self, level):
        return self.points >= level * 1000
evercraft/level.py
python
Copy code
class Level:
    def __init__(self, level=1):
        self.level = level

    def increase(self):
        self.level += 1
evercraft/race.py
python
Copy code
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
evercraft/class_.py
python
Copy code
class Class:
    def apply_class_bonuses(self, character):
        pass

class Fighter(Class):
    def apply_class_bonuses(self, character):
        character.hit_points += 5 * (character.level - 1)

class Rogue(Class):
    def apply_class_bonuses(self, character):
        character.hit_points += 5 * (character.level - 1)
        character.attack_bonus += character.abilities.dexterity_modifier

class Monk(Class):
    def apply_class_bonuses(self, character):
        character.hit_points += 5 * (character.level - 1)
        character.armor_class += character.abilities.wisdom_modifier

class Paladin(Class):
    def apply_class_bonuses(self, character):
        character.hit_points += 8 * (character.level - 1)
evercraft/weapon.py
python
Copy code
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
evercraft/armor.py
python
Copy code
class Armor:
    def __init__(self, name, armor_class_bonus):
        self.name = name
        self.armor_class_bonus = armor_class_bonus

class LeatherArmor(Armor):
    def __init__(self):
        super().__init__(name="Leather Armor", armor_class_bonus=2)
evercraft/item.py
python
Copy code
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
tests/init.py
This file can be left empty or used to initialize the package.

tests/test_abilities.py
python
Copy code
import unittest
from evercraft.abilities import Abilities

class TestAbilities(unittest.TestCase):
    def test_strength_modifier(self):
        abilities = Abilities(strength=12)
        self.assertEqual(abilities.strength_modifier, 1)

if __name__ == '__main__':
    unittest.main()
tests/test_alignment.py
python
Copy code
import unittest
from evercraft.alignment import Alignment

class TestAlignment(unittest.TestCase):
    def test_valid_alignment(self):
        self.assertTrue(Alignment.is_valid('Good'))
        self.assertFalse(Alignment.is_valid('Bad'))

if __name__ == '__main__':
    unittest.main()
tests/test_character.py
python
Copy code
import unittest
from evercraft.character import Character

class TestCharacter(unittest.TestCase):
    def test_character_creation(self):
        char = Character("Aragorn", "Good")
        self.assertEqual(char.name, "Aragorn")
        self.assertEqual(char.alignment, "Good")
        self.assertEqual(char.hit_points, 5)
        self.assertEqual(char.level, 1)

if __name__ == '__main__':
    unittest.main()
tests/test_combat.py
python
Copy code
import unittest
from evercraft.character import Character
from evercraft.combat import roll_die

class TestCombat(unittest.TestCase):
    def test_attack_success(self):
        char1 = Character("Aragorn", "Good")
        char2 = Character("Goblin", "Evil")
        result = char1.attack(char2, 20)
        self.assertTrue(result)
        self.assertEqual(char2.hit_points, 4)

if __name__ == '__main__':
    unittest.main()
tests/test_experience.py
python
Copy code
import unittest
from evercraft.experience import Experience

class TestExperience(unittest.TestCase):
    def test_gain_experience(self):
        exp = Experience()
        exp.add(100)
        self.assertEqual(exp.points, 100)

if __name__ == '__main__':
    unittest.main()
tests/test_level.py
python
Copy code
import unittest
from evercraft.level import Level

class TestLevel(unittest.TestCase):
    def test_level_up(self):
        level = Level()
        level.increase()
        self.assertEqual(level.level, 2)

if __name__ == '__main__':
    unittest.main()
tests/test_race.py
python
Copy code
import unittest
from evercraft.character import Character
from evercraft.race import Orc, Elf

class TestRace(unittest.TestCase):
    def test_orc_modifiers(self):
        char = Character("Gor", "Evil")
        orc = Orc()
        orc.apply_modifiers(char)
        self.assertEqual(char.abilities.strength, 12)
        self.assertEqual(char.abilities.intelligence, 9)

    def test_elf_modifiers(self):
        char = Character("Legolas", "Good")
        elf = Elf()
        elf.apply_modifiers(char)
        self.assertEqual(char.abilities.dexterity, 11)
        self.assertEqual(char.abilities.constitution, 9)

if __name__ == '__main__':
    unittest.main()
tests/test_class_.py
python
Copy code
import unittest
from evercraft.character import Character
from evercraft.class_ import Fighter, Rogue

class TestClass(unittest.TestCase):
    def test_fighter_class(self):
        char = Character("Conan", "Good")
        fighter = Fighter()
        fighter.apply_class_bonuses(char)
        self.assertEqual(char.hit_points, 15)

    def test_rogue_class(self):
        char = Character("Shadow", "Neutral")
        rogue = Rogue()
        rogue.apply_class_bonuses(char)
        self.assertEqual(char.attack_bonus, 1)

if __name__ == '__main__':
    unittest.main()
tests/test_weapon.py
python
Copy code
import unittest
from evercraft.weapon import Longsword

class TestWeapon(unittest.TestCase):
    def test_longsword_damage(self):
        sword = Longsword()
        self.assertEqual(sword.damage, 5)

if __name__ == '__main__':
    unittest.main()
tests/test_armor.py
python
Copy code
import unittest
from evercraft.armor import LeatherArmor

class TestArmor(unittest.TestCase):
    def test_leather_armor(self):
        armor = LeatherArmor()
        self.assertEqual(armor.armor_class_bonus, 2)

if __name__ == '__main__':
    unittest.main()
tests/test_item.py
python
Copy code
import unittest
from evercraft.item import RingOfProtection

class TestItem(unittest.TestCase):
    def test_ring_of_protection(self):
        ring = RingOfProtection()
        self.assertEqual(ring.armor_class_bonus, 2)

if __name__ == '__main__':
    unittest.main()
README.md
markdown
Copy code
# EverCraft Kata

This project is a domain model for the EverCraft Kata, an exercise for building out a domain model for an MMORPG called EverCraft.

## Project Structure

The project is organized as follows:

evercraft_kata/
├── evercraft/
│ ├── init.py
│ ├── abilities.py
│ ├── alignment.py
│ ├── character.py
│ ├── combat.py
│ ├── experience.py
│ ├── level.py
│ ├── race.py
│ ├── class_.py
│ ├── weapon.py
│ ├── armor.py
│ └── item.py
├── tests/
│ ├── init.py
│ ├── test_abilities.py
│ ├── test_alignment.py
│ ├── test_character.py
│ ├── test_combat.py
│ ├── test_experience.py
│ ├── test_level.py
│ ├── test_race.py
│ ├── test_class_.py
│ ├── test_weapon.py
│ ├── test_armor.py
│ └── test_item.py
└── README.md


## How to Run Tests

To run the tests, navigate to the project root and run:

```sh
python -m unittest discover tests