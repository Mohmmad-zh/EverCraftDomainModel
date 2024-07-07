import unittest
from evercraft.weapon import Longsword

class TestWeapon(unittest.TestCase):
    def test_longsword_damage(self):
        sword = Longsword()
        self.assertEqual(sword.damage, 5)

if __name__ == '__main__':
    unittest.main()
