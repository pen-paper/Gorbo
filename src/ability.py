# Targeting flags. MUTIPLE means it can hit multiple enemies in one area.
FRONT = 1
MIDDLE = 2
BACK = 4
MULTIPLE = 8

class Ability(object):
    def __init__(self, name, damage, cooldown, target):
        self.damage = damage
        self.cooldown = cooldown
        self.target = target
