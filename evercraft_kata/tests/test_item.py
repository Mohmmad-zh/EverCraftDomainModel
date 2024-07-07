import unittest
from evercraft.item import RingOfProtection

class TestItem(unittest.TestCase):
    def test_ring_of_protection(self):
        ring = RingOfProtection()
        self.assertEqual(ring.armor_class_bonus, 2)

if __name__ == '__main__':
    unittest.main()
