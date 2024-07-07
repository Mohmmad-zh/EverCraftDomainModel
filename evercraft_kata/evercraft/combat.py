def roll_die(sides=20):
    import random
    return random.randint(1, sides)
class Combat:
    @staticmethod
    def attack(attacker, defender, roll):
        if roll == 20 or roll + attacker.abilities.strength_modifier >= defender.armor_class:
            damage = 1 + attacker.abilities.strength_modifier
            if roll == 20:
                damage *= 2
            defender.hit_points -= max(1, damage)  # Ensure damage is at least 1
            return True
        return False
