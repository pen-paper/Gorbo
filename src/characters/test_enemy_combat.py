import pyglet
from . import character


class TestEnemyCombat(character.Character):
    def __init__(self, core):
        super().__init__(core, pyglet.resource.image("test_enemy.png"), 12, 12, 12)
        self.dead = False

    def attack(self, attack):
        self.dead = True
