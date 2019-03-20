import pyglet
from . import character


class TestCharacter(character.Character):
    def __init__(self, core):
        super().__init__(core, pyglet.resource.image("test_person.png"), 0, 1, -3)


    def key_press(self, key):
        if key == pyglet.window.key.A:
            self.vx -= 1
        elif key == pyglet.window.key.D:
            self.vx += 1
        elif key == pyglet.window.key.W:
            self.vz -= 1
        elif key == pyglet.window.key.S:
            self.vz += 1

    def key_release(self, key):
        if key == pyglet.window.key.A:
            self.vx += 1
        elif key == pyglet.window.key.D:
            self.vx -= 1
        elif key == pyglet.window.key.W:
            self.vz += 1
        elif key == pyglet.window.key.S:
            self.vz -= 1
        
