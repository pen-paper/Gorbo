import pyglet


class Game(pyglet.window.Window):
    def __init__(self):
        super().__init__()
        self.label = pyglet.text.Label('Le Game')
        self.label.x = 320
        self.label.y = 240
        self.label.anchor_x = 'center'
        self.label.anchor_y = 'center'

    def on_draw(self):
        self.clear()
        self.label.draw()

    def mainloop(self):
        pyglet.app.run()
