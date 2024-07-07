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
