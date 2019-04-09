import pyglet
from . import event


PERSPECTIVE = 0
ORTHOGONAL = 1


class Game(pyglet.window.Window):
    def __init__(self):
        super().__init__(visible=False, resizable=True)
        self.mode = None
        self.view = ORTHOGONAL
        pyglet.resource.path = ["/res/images", "/res/sounds", "/res/music"]
        pyglet.resource.reindex()
        self.keyhandler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keyhandler)

    def start_mode(self, mode):
        if self.mode is not None:
            self.mode.send_event(event.PauseEvent(), [self.mode])
        last_mode = self.mode
        self.mode = mode
        self.mode.setup(self, last_mode)

    def restore_mode(self, mode):
        self.mode = mode
        self.mode.send_event(event.UnPauseEvent(), [self.mode])

    def set_view(self, view):
        self.view = view
        if view == PERSPECTIVE:
            self.set_perspective()
        else:
            self.set_ortho()

    def on_draw(self):
        self.clear()
        self.mode.draw()

    def on_mouse_release(self, x, y, button, modifiers):
        self.mode.send_event(event.MouseUpEvent(x=x, y=y, button=button, modifiers=modifiers))

    def on_key_press(self, symbol, modifiers):
        self.mode.send_event(event.KeyDownEvent(key=key, modifiers=modifiers))

    def on_key_release(self, symbol, modifiers):
        self.mode.send_event(event.KeyUpEvent(key=key, modifiers=modifiers))

    def on_close(self):
        self.mode.send_event(event.QuitEvent(), [self.mode])

    def on_resize(self, width, height):
        #self._width = width
        #self._height = height
        if self.view == PERSPECTIVE:
            self.set_perspective()
        else:
            self.set_ortho()
        return pyglet.event.EVENT_HANDLED

    def set_ortho(self):
        width, height = self.get_size()
        pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)
        pyglet.gl.glViewport(0, 0, width, height)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glOrtho(0, width, 0, height, -1, 1)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def set_perspective(self):
        width, height = self.get_size()
        pyglet.gl.glEnable(pyglet.gl.GL_DEPTH_TEST)
        pyglet.gl.glViewport(0, 0, width, height)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.gluPerspective(65, width/height, 0.1, 1000)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def update(self, dt):
        self.mode.send_event(event.UpdateEvent(dt=dt))

    def mainloop(self):
        if self.mode is None:
            print("Error: No mode started.")
            print("Try starting the main menu.")
            return
        self.set_visible()
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()

    def quit(self):
        pyglet.app.exit()
