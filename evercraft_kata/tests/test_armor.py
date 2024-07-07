import unittest
from evercraft.armor import LeatherArmor

class TestArmor(unittest.TestCase):
    def test_leather_armor(self):
        armor = LeatherArmor()
        self.assertEqual(armor.armor_class_bonus, 2)

if __name__ == '__main__':
    unittest.main()
