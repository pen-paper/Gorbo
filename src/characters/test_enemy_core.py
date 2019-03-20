from . import character_core
from . import ability
from . import test_enemy
from ..modes import combat


class TestEnemyCore(character_core.CharacterCore):
    def __init__(self):
        super().__init__()
        self._abilities = [ability.Ability("Poke", damage=10, cooldown=0, target=ability.FRONT)]
        self._overworld = test_enemy.TestEnemy(self)
        self._combat = test_enemy.TestEnemy(self)

    @property
    def abilities(self):
        return self._abilities

    @property
    def overworld_sprite(self):
        return self._overworld

    @property
    def combat_sprite(self):
        return self._combat

    @property
    def combat_arena(self):
        return combat.TestCombat(self)
