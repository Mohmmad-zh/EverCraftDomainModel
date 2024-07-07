import unittest
from evercraft.abilities import Abilities

class TestAbilities(unittest.TestCase):
    def test_strength_modifier(self):
        abilities = Abilities(strength=12)
        self.assertEqual(abilities.strength_modifier, 1)

if __name__ == '__main__':
    unittest.main()
