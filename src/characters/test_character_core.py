from . import character_core
from . import ability
from . import test_character


class TestCharacterCore(character_core.CharacterCore):
    def __init__(self):
        super().__init__()
        self._abilities = [ability.Ability("Poke", damage=10, cooldown=0, target=ability.FRONT)]
        self._overworld = test_character.TestCharacter(self)
        self._combat = test_character.TestCharacter(self)

    @property
    def abilities(self):
        return self._abilities

    @property
    def overworld_sprite(self):
        return self._overworld

    @property
    def combat_sprite(self):
        return self._combat
