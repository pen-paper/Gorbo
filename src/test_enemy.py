import pyglet
from . import character


class TestEnemy(character.Character):
    def __init__(self):
        super().__init__(pyglet.resource.image("test_enemy.png"), -0.5, -0.5, -3.5)

