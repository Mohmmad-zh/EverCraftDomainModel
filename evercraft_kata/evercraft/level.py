# level.py

class Level:
    def __init__(self, initial_level=1):
        self.current_level = initial_level

    def increase(self):
        self.current_level += 1

    def calculate_hit_points(self, constitution_modifier):
        return 5 + constitution_modifier  # Adjust as per your rules

    @property
    def level(self):
        return self.current_level
