import pyglet


class TextureGroup(pyglet.graphics.Group):
    """Class for using a texture."""
    def __init__(self, texture):
        super().__init__()
        self.texture = texture

    def set_state(self):
        pyglet.gl.glEnable(self.texture.target)
        pyglet.gl.glBindTexture(self.texture.target, self.texture.id)

    def unset_state(self):
        pyglet.gl.glDisable(self.texture.target)

    def __eq__(self, other):
        if not isinstance(other, TextureGroup):
            return False
        return other.texture.target == self.texture.target
    
    def __hash__(self):
        return hash(self.texture)


class SpriteGroup(pyglet.graphics.Group):
    """Class for using a specific part of a texture.

    The two-layer group structure created by these classes allows
    sprites using the same underlying texture to be grouped, while
    still giving each sprite the texture region it needs.
    """
    def __init__(self, texture, x, y, z):
        super().__init__()
        self.texture = texture
        self.x = x
        self.y = y
        self.z = z

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
        pyglet.gl.glPushMatrix()
        pyglet.gl.glTranslatef(self.x, self.y, self.z)

    def unset_state(self):
        pyglet.gl.glMatrixMode(pyglet.gl.GL_TEXTURE)
        pyglet.gl.glPopMatrix()
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
        pyglet.gl.glPopMatrix()
        pyglet.gl.glDisable(self.texture.target)
    
    def __eq__(self, other):
        if not isinstance(other, SpriteGroup):
            return False
        #return self.z == other.z
        return False

    def __lt__(self, other):
        if not isinstance(other, SpriteGroup):
            return False
        return self.z < other.z

    def __gt__(self, other):
        if not isinstance(other, SpriteGroup):
            return True
        return self.z > other.z
 
    def __hash__(self):
        return hash(self.texture)
        

class BaseSprite(object):
    """Base class for all Sprites.

    Characters, walls, etc. use `ModelSprite`, menu items use 
    `DisplaySprite`, and ground (heightmap) sprites use `GroundSprite`.
    """
    def __init__(self, controller, texture, x, y, z=0):
        self.controller = controller
        self.texture = texture
        self.group = None
        self.x = x
        self.y = y
        self.z = z
        if self.texture is not None:
            self.group = SpriteGroup(texture, x, y, z)
        
    def create_vertex_list(self, batch):
        raise NotImplementedError("If you don't want it to appear, `pass`")

    def handle_event(self, event):
        if type(event) in self.controller.handlers:
            self.controller.handlers[type(event)](event)

    @property
    def x(self):
        if self.group is not None:
            return self.group.x
 
    @x.setter
    def x(self, value):
        if self.group is not None:
            self.group.x = value

    @property
    def y(self):
        if self.group is not None:
            return self.group.y
 
    @y.setter
    def y(self, value):
        if self.group is not None:
            self.group.y = value

    @property
    def z(self):
        if self.group is not None:
            return self.group.z
 
    @z.setter
    def z(self, value):
        if self.group is not None:
            self.group.z = value

    

class DisplaySprite(BaseSprite):
    """Base class for 2d sprites."""
    pass


class ModelSprite(BaseSprite):
    """Base class for 3d sprites."""
    def __init__(self, model, x, y, z, controller, texture):
        self.model = model
        super().__init__(controller, texture, x, y, z)
        
    def create_vertex_list(self, batch):
        self.vertex_list = batch.add_indexed(
            self.model.num_verts,
            pyglet.gl.GL_TRIANGLES,
            self.group,
            self.model.indices,
            ("v3f", self.model.vertices),
            ("t2f", self.model.tex_coords),
            ("n3f", self.model.normals),
            ("c3B", (127,)*self.model.num_verts*3))

    def collision(self, other):
        pass


class GroundSprite(ModelSprite):
    """Base class for heightmap sprites."""
    def __init__(self, controller, model, mode, texture):
        super().__init__(controller, model, mode, texture)

    def create_vertex_list(self):
        # TODO: Actually load the model
        super().create_vertex_list()

    def get_heights(self, x, y):
        # TODO: Add the fancy height getting code from earlier.
        return []
