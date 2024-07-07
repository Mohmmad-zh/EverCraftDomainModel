import unittest
from evercraft.level import Level

class TestLevel(unittest.TestCase):
    def test_level_up(self):
        level = Level()
        level.increase()
        self.assertEqual(level.level, 2)

if __name__ == '__main__':
    unittest.main()
