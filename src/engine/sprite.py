import pyglet


class TextureGroup(pyglet.graphics.Group):
    """Class for using a texture."""
    def __init__(self, texture):
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


class SpriteGroup(pyglet.graphics.Group):
    """Class for using a specific part of a texture.

    The two-layer group structure created by these classes allows
    sprites using the same underlying texture to be grouped, while
    still giving each sprite the texture region it needs.
    """
    def __init__(self, texture):
        super().__init__(parent=TextureGroup(texture))
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
        pyglet.gl.glMopMatrix()
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
        

class BaseSprite(object):
    """Base class for all Sprites.

    Characters, walls, etc. use `ModelSprite`, menu items use 
    `DisplaySprite`, and ground (heightmap) sprites use `GroundSprite`.
    """
    def __init__(self, controller, mode, texture):
        self.controller = controller
        self.mode = mode
        self.texture = texture
        if self.texture is not None:
            self.group = SpriteGroup(texture)
        else:
            self.group = None
        self.create_vertex_list()
        self.handlers = {}
        
    def create_vertex_list(self):
        raise NotImplementedError("If you don't want it to appear, `pass`")

    def handle_event(self, event):
        if type(event) in self.handlers:
            self.handlers[type(event)](event)
    

class DisplaySprite(BaseSprite):
    """Base class for 2d sprites."""
    pass


class ModelSprite(BaseSprite):
    """Base class for 3d sprites."""
    def __init__(self, controller, model, mode, texture):
        self.model = model
        super().__init__(controller, mode, texture)
        
    def create_vertex_list(self):
        # TODO: Actaully load a model.
        super().create_vertex_list()

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
