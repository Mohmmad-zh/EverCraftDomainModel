import unittest
from evercraft.experience import Experience

class TestExperience(unittest.TestCase):
    def test_gain_experience(self):
        exp = Experience()
        exp.add(100)
        self.assertEqual(exp.points, 100)

if __name__ == '__main__':
    unittest.main()
