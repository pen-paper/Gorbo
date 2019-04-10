import pyglet
from . import event


class Mode(object):
    """Base class for all game modes."""

    def __init__(self):
        self.game = None
        self.last_mode = None
        self.batch = pyglet.graphics.Batch()
        self.sprites = []
        self.handlers = {
            event.DeleteSpriteEvent: self.destroy_sprite,
            event.CreateSpriteEvent: self.create_sprite,
            event.QuitEvent: self.quit,
        }

    def setup(self, game, last_mode):
        self.game = game
        self.last_mode = last_mode

    def send_event(self, e_event, sprites=None):
        if sprites is None:
            sprites = self.sprites
        for sprite in sprites:
            sprite.handle_event(e_event)

    def handle_event(self, e_event):
        if type(e_event) in self.handlers:
            self.handlers[type(e_event)](e_event)

    def create_sprite(self, s_event):
        self.sprites.append(s_event.sprite)

    def destroy_sprite(self, d_event):
        self.sprites.remove(d_event.sprite)

    def quit(self, event):
        self.game.quit()

    def draw(self):
        print("Drawing a frame!")
        self.batch.draw()

