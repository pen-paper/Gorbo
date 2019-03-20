# Targeting flags. MUTIPLE means it can hit multiple enemies in one area.
FRONT = 1
MIDDLE = 2
BACK = 4
MULTIPLE = 8


class Ability(object):
    def __init__(self):
        pass

    @property
    def name(self):
        pass

    @property
    def attack(self):
        pass

    @property
    def current_cooldown(self):
        pass

    @property
    def max_cooldown(self):
        pass

    @property
    def target_type(self):
        pass


class Attack(object):
    def __init__(self, amount):
        self.amount = amount
