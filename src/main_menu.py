import pyglet
from . import mode
from . import overworld


class MainMenu(mode.Mode):
    def __init__(self):
        super().__init__()
        self.background_group = pyglet.graphics.OrderedGroup(0)
        self.foreground_group = pyglet.graphics.OrderedGroup(1)

    def setup(self, game, last_mode):
        super().setup(game, last_mode)
        self.game.set_view(self.game.ORTHO)
        width, height = self.game.get_size()
        self.background = self.batch.add_indexed(4, pyglet.gl.GL_TRIANGLES,
                               self.background_group, [0, 1, 2, 0, 2, 3],
                               ("v3f", (width/8, height/8, 0.5,
                                        7*width/8, height/8, 0.5,
                                        7*width/8, 7*height/8, 0.5,
                                        width/8, 7*height/8, 0.5)),
                               ("c3B", (0, 0, 255, 0, 0, 255,
                                        0, 255, 0, 0, 255, 0)))
        self.title = pyglet.text.Label("Le Game", font_size=36,
                                       batch=self.batch, group=self.foreground_group,
                                       anchor_x="center", anchor_y="bottom",
                                       x=width/2, y=3*height/4)
        self.button = self.batch.add_indexed(9, pyglet.gl.GL_TRIANGLES,
                                self.foreground_group, [0, 1, 2, 0, 2, 4, 0, 4, 3,
                                             3, 4, 5, 4, 6, 5, 5, 6, 8,
                                             6, 7, 8, 7, 6, 2, 7, 2, 1,
                                             6, 4, 2],
                                ("v2f", (width/3 - 10, height/3 - 6,
                                         width/3, height/3 - 12,
                                         width/3, height/3,
                                         width/3 - 10, 2*height/3 + 6,
                                         width/3, 2*height/3,
                                         width/3, 2*height/3 + 12,
                                         2*width/3, height/2,
                                         2*width/3 + 10, height/2 - 6,
                                         2*width/3 + 10, height/2 + 6)),
                                 ("c3B", (125, 0, 0, 64, 0, 0, 164, 32, 32,
                                          125, 0, 0, 255, 128, 128, 140, 16, 16,
                                          164, 32, 32, 64, 0, 0, 140, 16, 16)))

    def update(self, dt):
        width, height = self.game.get_size()
        self.background.vertices = (width/8, height/8, -0.5,
                                    7*width/8, height/8, -0.5,
                                    7*width/8, 7*height/8, -0.5,
                                    width/8, 7*height/8, -0.5)
        self.button.vertices = (width/3 - 10, height/3 - 6,
                                width/3, height/3 - 12,
                                width/3, height/3,
                                width/3 - 10, 2*height/3 + 6,
                                width/3, 2*height/3,
                                width/3, 2*height/3 + 12,
                                2*width/3, height/2,
                                2*width/3 + 10, height/2 - 6,
                                2*width/3 + 10, height/2 + 6)
        self.title.x = width/2
        self.title.y = 3*height/4

    def on_mouse_release(self, x, y, button, modifiers):
        self.game.start_mode(overworld.Overworld())
