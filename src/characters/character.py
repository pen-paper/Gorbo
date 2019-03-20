import pyglet


class Character(object):
    def __init__(self, core, texture, x, y, z):
        self.core = core
        self.texture = texture
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.w = self.texture.width / 200
        self.h = self.texture.height / 100
        self.vertex_list = None
        self.group = pyglet.sprite.SpriteGroup(self.texture, pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

    def add_to_batch(self, batch):
        if self.vertex_list is not None:
            self.vertex_list.delete()
        self.vertex_list = batch.add_indexed(4, pyglet.gl.GL_TRIANGLES, self.group,
                                             [0, 1, 2, 0, 2, 3],
                                             "v3f/stream", 
                                             ("t3f/static", self.texture.tex_coords))
        self.update_position()

    def update_position(self):
        self.vertex_list.vertices[:] = (self.x-self.w, self.y, self.z,
                                        self.x+self.w, self.y, self.z,
                                        self.x+self.w, self.y+self.h, self.z,
                                        self.x-self.w, self.y+self.h, self.z)

    def update(self, overworld, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.z += self.vz * dt
        heights = overworld.get_heights(self.x, self.z)
        for height in heights:
            if height == self.y:
               break
            elif self.y < height < self.y + self.h:
               self.y = height
               break
        else:
            self.vy = -1
        self.update_position()
