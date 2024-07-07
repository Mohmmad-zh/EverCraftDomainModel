# test_combat.py

import unittest
from evercraft.character import Character

class TestCombat(unittest.TestCase):
    def test_attack_success(self):
        char1 = Character("Aragorn", "Good")
        char2 = Character("Goblin", "Evil")
        char2.hit_points = 5  # Set initial hit points for testing purposes
        result = char1.attack(char2, 20)  # Assuming a critical hit with roll 20
        self.assertTrue(result)
        self.assertEqual(char2.hit_points, 5)  # Adjust expected hit points based on damage calculation

if __name__ == '__main__':
    unittest.main()
