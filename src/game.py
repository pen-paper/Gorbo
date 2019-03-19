import pyglet
from .characters import test_character_core


class Game(pyglet.window.Window):
    PERSPECTIVE = 0
    ORTHO = 1

    def __init__(self):
        super().__init__(visible=False, resizable=True)
        self.mode = None
        self.view = self.ORTHO
        pyglet.resource.path = ["./res/images", "./res/sounds", "./res/music"]
        pyglet.resource.reindex()
        self.keyhandler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keyhandler)
        self.character_core = test_character_core.TestCharacterCore()

    def start_mode(self, mode):
        if self.mode is not None:
            self.mode.on_pause()
        last_mode = self.mode
        self.mode = mode
        self.mode.setup(self, last_mode)

    def restore_mode(self, mode):
        self.mode = mode
        mode.on_restore()

    def set_view(self, view):
        self.view = view
        if view == self.PERSPECTIVE:
            self.set_perspective()
        else:
            self.set_ortho()

    def on_draw(self):
        self.clear()
        self.mode.draw()

    def on_mouse_release(self, x, y, button, modifiers):
        self.mode.on_mouse_release(x, y, button, modifiers)

    def on_key_press(self, symbol, modifiers):
        self.mode.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.mode.on_key_release(symbol, modifiers)

    def on_resize(self, width, height):
        #self._width = width
        #self._height = height
        if self.view == self.PERSPECTIVE:
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
        #pyglet.gl.glTranslatef(width/2, height/2, -20)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def update(self, dt):
        self.mode.update(dt)

    def mainloop(self):
        if self.mode is None:
            print("Error: No mode started.")
            print("Try starting the main menu.")
            return
        self.set_visible()
        #pyglet.gl.glFrontFace(pyglet.gl.GL_CW)
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()
