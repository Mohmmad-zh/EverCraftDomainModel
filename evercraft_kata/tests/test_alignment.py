import unittest
from evercraft.alignment import Alignment

class TestAlignment(unittest.TestCase):
    def test_valid_alignment(self):
        self.assertTrue(Alignment.is_valid('Good'))
        self.assertFalse(Alignment.is_valid('Bad'))

if __name__ == '__main__':
    unittest.main()
