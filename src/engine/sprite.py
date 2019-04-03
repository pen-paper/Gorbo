import pyglet


class TextureGroup(pyglet.glaphics.Group):
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
    def __init__(self, controller, mode, texture):
        self.controller = controller
        self.mode = mode
        self.texture = texture
        self.group = SpriteGroup(texture)
        self.create_vertex_list()
        
    def create_vertex_list(self):
        raise NotImplementedError("If you don't want it to appear, `pass`")

    def update(self):
        pass

    def button_up(self):
        pass

    def button_down(self):
        pass

    

class DisplaySprite(BaseSprite):
    pass


class ModelSprite(BaseSprite):
    def __init__(self, controller, model, mode, texture):
        self.model = model
        super().__init__(controller, mode, texture)
        
    def create_vertex_list(self):
        # TODO: Actaully load a model.
        super().create_vertex_list()

    def collision(self, other):
        pass


class GroundSprite(BaseSprite):
    def __init__(self, controller, mode, model, texture):
        self.model = model
        super().__init__(controller, mode, texture)

    def create_vertex_list(self):
        # TODO: Actually load the model
        super().create_vertex_list()

    def get_heights(self, x, y):
        # TODO: Add the fance height getting code from earlier.
        return []
