import pyglet
from . import mode
from . import characters


class OverworldGroundTextureGroup(pyglet.graphics.Group):
    def __init__(self, texture):
        super().__init__()
        self.texture = texture

    def set_state(self):
        pyglet.gl.glEnable(self.texture.target)
        pyglet.gl.glBindTexture(self.texture.target, self.texture.id)
        t = self.texture.tex_coords
        x, y = t[:2]
        w = t[6] - x
        h = t[7] - y
        pyglet.gl.glMatrixMode(pyglet.gl.GL_TEXTURE)
        pyglet.gl.glPushMatrix()
        pyglet.gl.glTranslatef(x, y, 0)
        pyglet.gl.glScalef(w, h, 1)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def unset_state(self):
        pyglet.gl.glDisable(self.texture.target)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_TEXTURE)
        pyglet.gl.glPopMatrix()
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)


class Overworld(mode.Mode):
    def __init__(self):
        super().__init__()
        self.ground_texture = None
        self.ground_group = None
        self.ground = None
        self.character = characters.TestCharacter()
        # TODO: Add variables specific to the Overworld.

    def setup(self, game, last_mode):
        super().setup(game, last_mode)
        self.game.set_view(self.game.PERSPECTIVE)
        self.character.add_to_batch(self.batch)
        self.ground_texture = pyglet.resource.image("overworld_ground.png")
        self.ground_group = OverworldGroundTextureGroup(self.ground_texture)
        #  self.ground = self.batch.add_indexed(4, pyglet.gl.GL_TRIANGLES, self.ground_group, [0, 2, 1, 0, 3, 2], "v3f", "t2f")
        #  self.ground.vertices = (-1.5, -1.0, -2, 1.5, -1.0, -2, 1.5, -1.0, -5, -1.5, -1.0, -5)
        #  #  self.ground.colors = (255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255)
        #  self.ground.tex_coords = (0, 0, 1, 0, 1, 1, 1, 0)
        self.ground = self.batch.add_indexed(16, pyglet.gl.GL_TRIANGLES, 
                                             self.ground_group,
                                             [0, 4, 5, 0, 5, 1, 1, 5, 6,
                                              1, 6, 2, 2, 6, 7, 2, 7, 3,
                                              4, 8, 9, 4, 9, 5, 5, 9, 10,
                                              5, 10, 6, 6, 10, 11, 6, 11, 7,
                                              8, 12, 13, 8, 13, 9, 9, 13, 14,
                                              9, 14, 10, 10, 14, 15, 10, 15, 11
                                             ],
                                             "v3f/static", "t2f/static")
        self.ground.vertices = (-1.5, -1, -2,     -0.5, -0.5, -2,    0.50, -0.5, -2,   1.50, -1, -2,
                                -1.50, -0.5, -2.5,  -.50, -0.25, -2.5,  .50, -0.25, -2.5,  1.50, -0.5, -2.5,
                                -1.50, -0.5, -3.5,  -.50, -0.25, -3.5,  .50, -0.25, -3.5,  1.50, -0.5, -3.5,
                                -1.50, -1, -4,    -.50, -0.5, -4,    .50, -0.5, -4,    1.50, -1, -4)
        self.ground.tex_coords = (0, 0, 0.25, 0, 0.75, 0, 1, 0, 0, 0.25,
                                  0.25, 0.25, 0.75, 0.25, 1, 0.25, 0, 0.75,
                                  0.25, 0.75, 0.75, 0.75, 1, 0.75, 0, 1, 
                                  0.25, 1, 0.75, 1, 1, 1)
        #  self.ground.colors = (255, 0, 0) * 16

    def get_heights(self, x, z):
        heights = []
        for triangle in range(len(self.ground.indices)//3):
            i1, i2, i3 = self.ground.indices[triangle*3:triangle*3+3]
            x1, y1, z1 = self.ground.vertices[i1*3:i1*3+3]
            x2, y2, z2 = self.ground.vertices[i2*3:i2*3+3]
            x3, y3, z3 = self.ground.vertices[i3*3:i3*3+3]
            if min(x1, x2, x3) > x or max(x1, x2, x3) < x or min(z1, z2, z3) > z or max(z1, z2, z3) < z:
                continue
            w1 = ((z2-z3)*(x-x3)+(x3-x2)*(z-z3))/((z2-z3)*(x1-x3)+(x3-x2)*(z1-z3))
            w2 = ((z3-z1)*(x-x3)+(x1-x3)*(z-z3))/((z2-z3)*(x1-x3)+(x3-x2)*(z1-z3))
            w3 = 1 - w1 - w2
            if min(w1, w2, w3) < 0:
                continue
            heights.append(y1*w1+y2*w2+y3*w3)
        return heights

    def update(self, dt):
        # TODO: Add game logic for the overworld.
        self.character.update(self, dt)

    def draw(self):
        # TODO: Add redrawing to the overworld.
        pyglet.gl.glLoadIdentity()
        pyglet.gl.gluLookAt(self.character.x, self.character.y+1+self.character.h, self.character.z+2, self.character.x, self.character.y+self.character.h, self.character.z, 0, 1, 0)
        super().draw()

    def on_key_press(self, symbol, modifiers):
        self.character.key_press(symbol)

    def on_key_release(self, symbol, modifiers):
        self.character.key_release(symbol)
