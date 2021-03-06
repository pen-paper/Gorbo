from .. import character_core
from ...abilities import test_ability
from . import test_enemy
from . import test_enemy_combat
from . import test_combat


class TestEnemyCore(character_core.CharacterCore):
    def __init__(self):
        super().__init__()
        self._abilities = [test_ability.TestAbility()]
        self._overworld = test_enemy.TestEnemy(self)
        self._combat = test_enemy_combat.TestEnemyCombat(self)

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
        return test_combat.TestCombat(self)
