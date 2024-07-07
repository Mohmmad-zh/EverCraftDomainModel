class Experience:
    def __init__(self):
        self.points = 0

    def gain_experience(self, amount):
        self.points += amount

    # Optionally, if you need to increment by a specific value
    def add(self, value):
        self.points += value
