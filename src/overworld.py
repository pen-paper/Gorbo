import pyglet
from . import mode


class OverworldGroundTextureGroup(pyglet.graphics.Group):
    def __init__(self, texture):
        super().__init__()
        self.texture = texture

    def set_state(self):
        pyglet.gl.glEnable(self.texture.target)
        pyglet.gl.glBindTexture(self.texture.target, self.texture.id)

    def unset_state(self):
        pyglet.gl.glDisable(self.texture.target)


class Overworld(mode.Mode):
    def __init__(self):
        super().__init__()
        self.ground_texture = None
        self.ground_group = None
        self.ground = None
        # TODO: Add variables specific to the Overworld.

    def setup(self, game, last_mode):
        super().setup(game, last_mode)
        self.game.set_view(self.game.PERSPECTIVE)
        self.ground_texture = pyglet.resource.image("overworld_ground.png")
        self.ground_group = OverworldGroundTextureGroup(self.ground_texture)
        self.ground = self.batch.add_indexed(4, pyglet.gl.GL_TRIANGLES, self.ground_group, [0, 2, 1, 0, 3, 2], "v3f", "t2f")
        self.ground.vertices = (-1.5, -1.0, -2, 1.5, -1.0, -2, 1.5, -1.0, -5, -1.5, -1.0, -5)
        #  self.ground.colors = (255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255)
        t = self.ground_texture.tex_coords
        self.ground.tex_coords = (t[0], t[1], t[3], t[4], t[6], t[7], t[9], t[10])
        #  self.ground = self.batch.add_indexed(16, pyglet.gl.GL_TRIANGLES, 
        #                                       self.ground_group,
        #                                       [0, 4, 5, 0, 5, 1, 1, 5, 6,
        #                                        1, 6, 2, 2, 6, 7, 2, 7, 3,
        #                                        4, 8, 9, 4, 9, 5, 5, 9, 10,
        #                                        5, 10, 6, 6, 10, 11, 6, 11, 7,
        #                                        8, 12, 13, 1, 13, 9, 9, 13, 14,
        #                                        9, 14, 10, 10, 14, 15, 10, 15, 11
        #                                       ],
        #                                       "v3f/static", "t2f/static", "c3B/static")
        #  self.ground.vertices = (-150, -250, -150, -50, 250, -150, 50, -250, -150, 150, 250, -150,
        #                          -150, 0, -50, -50, 0, -50, 50, 0, -50, 150, 0, -150,
        #                          -150, 0, 50, -50, 0, 50, 50, 0, 50, 150, 0, 50,
        #                          -150, 250, 150, -50, 250, 150, 50, 250, 150, 150, 250, 150)
        #  self.ground.tex_coords = (0, 0, 0.25, 0, 0.75, 0, 1, 0, 0, 0.25,
        #                            0.25, 0.25, 0.75, 0.25, 1, 0.25, 0, 0.75,
        #                            0.25, 0.75, 0.75, 0.75, 1, 0.75, 0, 1, 
        #                            0.25, 1, 0.75, 1, 1, 1)
        #  self.ground.colors = (255, 0, 0) * 16

    def update(self, dt):
        # TODO: Add game logic for the overworld.
        pass

    def draw(self):
        # TODO: Add redrawing to the overworld.
        super().draw()
