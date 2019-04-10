import pyglet


from ..engine import DisplaySprite, Game


class MenuSprite(DisplaySprite):
    def create_vertex_list(self):
        print("Creating Triangle!")
        # pyglet.graphics._debug_graphics_batch = True
        game = Game()
        width = game.width
        height = game.height
        self.mode.batch.add_indexed(9, pyglet.gl.GL_TRIANGLES,
                                None, [0, 1, 2, 0, 2, 4, 0, 4, 3,
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

