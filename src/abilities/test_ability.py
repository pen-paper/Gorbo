from . import ability


class TestAbility(ability.Ability):
    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return "Poke"

    @property
    def attack(self):
        return ability.Attack(10)

    @property
    def max_cooldown(self):
        return 0

    @property
    def current_cooldown(self):
        return 0

    @property
    def target_type(self):
        return ability.FRONT
