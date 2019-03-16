import pyglet


class Mode(object):
    """Base class for all game modes."""

    def __init__(self):
        self.game = None
        self.last_mode = None
        self.batch = pyglet.graphics.Batch()

    def setup(self, game, last_mode):
        self.game = game
        self.last_mode = last_mode

    def update(self, dt):
        pass

    def draw(self):
        self.batch.draw()

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass
