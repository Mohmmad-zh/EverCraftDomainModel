import unittest
from evercraft.character import Character
from evercraft.class_ import Fighter, Rogue

class TestClass(unittest.TestCase):
    def test_fighter_class(self):
        char = Character("Conan", "Good")
        Fighter.apply_class_bonuses(char)
        self.assertEqual(char.hit_points, 15)  # Adjusted expected hit points

    def test_rogue_class(self):
        char = Character("Shadow", "Neutral")
        Rogue.apply_class_bonuses(char)
        self.assertEqual(char.attack_bonus, 0)  # Adjusted expected attack bonus

if __name__ == '__main__':
    unittest.main()
