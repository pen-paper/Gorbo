import pyglet
from . import event


class Mode(object):
    """Base class for all game modes.

    A Mode is an independent game environment: a menu, level, etc.
    Modes are responsible for telling the Game what projection to use,
    drawing all Sprites to the screen, managing the Sprites it
    contains, and for distributing events to all relevant Sprites.
    """

    def __init__(self):
        """Create a mode.

        By default, this gives each mode a batch for drawing sprites,
        a list of those sprites (initially empty), and a dictionary of
        event handlers. This works in the same way as for Sprites:
            self.handlers[<event_type>] = event_handler
        """
        self.game = None
        self.last_mode = None
        self.batch = pyglet.graphics.Batch()
        self.sprites = []
        self.handlers = {
            event.DeleteSpriteEvent: lambda e: self.destroy_sprite(e.sprite),
            event.CreateSpriteEvent: lambda e: self.create_sprite(e.sprite),
            event.QuitEvent: self.quit,
        }

    def setup(self, game, last_mode):
        """Prepare for activation.

        The default does very little, just enough bookkeeping to
        restore the previous mode later. Subclasses should also set the
        projection type here.
        """
        self.game = game
        self.last_mode = last_mode

    def send_event(self, e_event, sprites=None):
        """Distribute an event to Sprites.

        If `sprites` is given, it contains a list of the only sprites
        that should receive the event. This is for things like
        collisions, where only two sprites are involved. If not given,
        the event is given to all sprites iin the mode.
        """
        if sprites is None:
            sprites = self.sprites
        for sprite in sprites:
            sprite.handle_event(e_event)

    def handle_event(self, e_event):
        """Deal with an event.

        Modes do not handle very many events themselves, and currently
        these events must be sent directly via `send_event(e, [mode])`.
        
        Events that Modes can or should handle include:
          * PauseEvent, when another mode replaces this one,
          * UnPauseEvent, when the replacement mode finishes,
          * QuitEvent, when the user attempts to close the window
        """
        if type(e_event) in self.handlers:
            self.handlers[type(e_event)](e_event)

    def create_sprite(self, sprite):
        """Add a new sprite to the mode.

        This is done in response to a CreateSpriteEvent.
        """
        self.sprites.append(sprite)
        sprite.create_vertex_list(self.batch)

    def destroy_sprite(self, sprite):
        """Remove a sprite from the mode.

        This is done in response to a DeleteSpriteEvent.
        """
        self.sprites.remove(sprite)
        sprite.delete_vertex_lists()

    def quit(self, event):
        """Tell the game to exit.

        This is done in response to a QuitEvent. If you want something
        else to happen when closing, either override this method or
        assign a new event handler in `handlers`.
        """
        self.game.quit()

    def draw(self):
        """Redraw the scene.

        Pyglet batches should be used for all rendering. Geneerally,
        this method should be sufficient. If a mode requires both 2d
        and 3d sprites (e.g. a game with a HUD), those should be
        contained in two separate batches with calls to `game.set_view`
        between drawing them.
        """
        self.batch.draw()


class GameMode(Mode):
    """A mode containing a 3d game environment."""
    def __init__(self, ground, other):
        super().__init__()
        self.ground_sprites = []
        for g in ground:
            self.ground_sprites.append(g)
            self.create_sprite(g)
        for s in other:
            self.create_sprite(s)

    def setup(self, game, last_mode):
        super().setup(game, last_mode)

    def draw(self):
        self.game.set_perspective()
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.gluLookAt(0, 5, 9, 0, 1, 0, 0, 1, 0)
        self.batch.draw()

