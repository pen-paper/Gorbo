import pyglet
from . import character
from . import combat


class TestEnemy(character.Character):
    def __init__(self):
        super().__init__(pyglet.resource.image("test_enemy.png"), -0.5, -0.5, -3.5)
        self.just_faught = False

    def update(self, overworld, dt):
        super().update(overworld, dt)
        if self.x - self.w < overworld.character.x < self.x + self.w:
            if self.z - self.w < overworld.character.z < self.z + self.w:
                if not self.just_faught:
                    overworld.game.start_mode(combat.TestCombat())
                    self.just_faught = True
                return
        self.just_faught = False
