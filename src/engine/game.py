import pyglet
from . import event


PERSPECTIVE = 0
ORTHOGONAL = 1


class _Game(pyglet.window.Window):
    """The global object managing the entire game environment.

    This class should not be used directly; use the `Game` helper
    function to access the current game if it exists.

    `_Game` objects act as interfaces with the outer world (meaning 
    pyglet). They control the window, the projection, and the current
    mode. Any external events are sent to the current mode through the
    game object.
    """

    def __init__(self):
        """Create a Game."""
        super().__init__(visible=False, resizable=True)
        self.mode = None
        self.view = ORTHOGONAL
        pyglet.resource.path = ["/res/images", "/res/sounds", "/res/music"]
        pyglet.resource.reindex()
        self.keyhandler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keyhandler)

    def start_mode(self, mode):
        """ Activate `mode`.

        This function sets `mode` as the current mode, to be updated or
        redrawn. A previous mode, if any, is sent a PauseEvent and
        passed to the `setup` method of the new mode.

        When a mode finishes, it should call `restore_mode` to return
        to the previous mode.
        """
        if self.mode is not None:
            self.mode.send_event(event.PauseEvent(), [self.mode])
        last_mode = self.mode
        self.mode = mode
        self.mode.setup(self, last_mode)

    def restore_mode(self, mode):
        """ Switch back to a previous mode.

        This function sets `mode` as the current mode. It assumes that
        the mode was already used and was paused by another mode
        overriding it using `start_mode`. The mode is sent an 
        UnPauseEvent with no arguments.

        Any previous mode is discarded.
        """ 
        self.mode = mode
        self.mode.send_event(event.UnPauseEvent(), [self.mode])

    def set_view(self, view):
        """ Set the viewport to be either 3d or 2d.

        This method can be called at two different times, depending on
        the needs of the mode. If the mode uses 2d or 3d exclusively,
        it should call this only from the `setup` method or when
        responding to an UnPauseEvent. It the mode uses both, it should
        call this function twice during the `redraw` method.
        """
        self.view = view
        if view == PERSPECTIVE:
            self.set_perspective()
        else:
            self.set_ortho()

    def on_draw(self):
        """Redraw the screen."""
        self.clear()
        self.mode.draw()

    def on_mouse_release(self, x, y, button, modifiers):
        """Send a MouseUpEvent to the current mode."""
        self.mode.send_event(event.MouseUpEvent(
                       x=x, y=y, button=button, modifiers=modifiers))

    def on_key_press(self, key, modifiers):
        """Send a KeyDownEvent to the current mode."""
        self.mode.send_event(event.KeyDownEvent(
                       key=key, modifiers=modifiers))

    def on_key_release(self, key, modifiers):
        """Send a KeyUpEvent to the current mode."""
        self.mode.send_event(event.KeyUpEvent(
                       key=key, modifiers=modifiers))

    def on_close(self):
        """Send a QuitEvent to the current mode.

        The default event handler for this event in `Mode`s is to quit
        the game.
        """
        self.mode.send_event(event.QuitEvent(), [self.mode])

    def on_resize(self, width, height):
        """Adjust the projection to fit the new size.

        The current mode should probably be alerted.
        """
        #self._width = width
        #self._height = height
        if self.view == PERSPECTIVE:
            self.set_perspective()
        else:
            self.set_ortho()
        return pyglet.event.EVENT_HANDLED

    def set_ortho(self):
        """Create an orthographic (2d) projection."""
        width, height = self.get_size()
        pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)
        pyglet.gl.glViewport(0, 0, width, height)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glOrtho(0, width, 0, height, -1, 1)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def set_perspective(self):
        """Create a perspective (3d) projection."""
        width, height = self.get_size()
        pyglet.gl.glEnable(pyglet.gl.GL_DEPTH_TEST)
        pyglet.gl.glViewport(0, 0, width, height)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.gluPerspective(65, width/height, 0.1, 1000)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def update(self, dt):
        """Send an UpdateEvent to the current mode."""
        self.mode.send_event(event.UpdateEvent(dt=dt))

    def mainloop(self):
        """Run the game."""
        if self.mode is None:
            print("Error: No mode started.")
            print("Try starting the main menu.")
            return
        self.set_visible()
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()

    def quit(self):
        """Exit the game.
  
        This method is usually called my modes responding to a
        QuitEvent.
        """
        pyglet.app.exit()


_game = None

def Game():
    """Get the Game instance.

    If a Game instance has been created, return that. Otherwise, return
    the current Game. This allows Sprites and Controllers to access 
    game attributes such as the window size.
    """
    global _game
    if _game is None:
        _game = _Game()
    return _game
