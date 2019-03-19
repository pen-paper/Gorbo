from . import character_core
from . import ability


class TestCharacterCore(character_core.CharacterCore):
    def __init__(self):
        super().__init__()
        self._abilities = [ability.Ability("Poke", damage=10, cooldown=0, target=ability.FRONT)]

    @property
    def abilities(self):
        return self._abilities
