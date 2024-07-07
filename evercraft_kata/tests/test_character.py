import unittest
from evercraft.character import Character
from evercraft.experience import Experience  # Import Experience

class TestCharacter(unittest.TestCase):
    def test_character_creation(self):
        char = Character("Aragorn", "Good")
        self.assertEqual(char.name, "Aragorn")
        self.assertEqual(char.alignment, "Good")

if __name__ == '__main__':
    unittest.main()