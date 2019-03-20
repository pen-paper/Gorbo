import pyglet
from . import mode
from . import overworld
from ..characters import test_enemy
from ..characters import test_character


class TestCombat(mode.Mode):
    def __init__(self, character):
        super().__init__()
        self.enemy_character = character
        self.positions = [[None, None, None] for y in range(6)]
        self.abilities_list = []
        self.ability_labels = pyglet.graphics.Batch()

    def setup(self, game, last_mode):
        super().setup(game, last_mode)
        game.set_view(game.PERSPECTIVE)
        self.character = game.character_core.combat_sprite
        self.enemy = self.enemy_character.combat_sprite
        self.character.x = -0.75
        self.enemy.x = 0.75
        self.character.y = 0
        self.enemy.y = 0
        self.character.z = -3.25
        self.enemy.z = -3.25
        self.character.add_to_batch(self.batch)
        self.enemy.add_to_batch(self.batch)
        self.ground_texture = pyglet.resource.image("overworld_ground.png")
        self.ground_group = overworld.OverworldGroundTextureGroup(self.ground_texture)
        self.ground = self.batch.add_indexed(24, pyglet.gl.GL_TRIANGLES, self.ground_group,
                                             [0, 1, 2, 0, 2, 3, 4, 5, 6, 4, 6, 7, 
                                              8, 9, 10, 8, 10, 11, 12, 13, 14, 12, 14, 15,
                                              16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23],
                                             "v3f", "t2f")
        self.ground.tex_coords = (0, 0, 0, 1, 1, 1, 1, 0,
                                  0, 0, 0, 1, 1, 1, 1, 0,
                                  0, 0, 0, 1, 1, 1, 1, 0,
                                  0, 0, 0, 1, 1, 1, 1, 0,
                                  0, 0, 0, 1, 1, 1, 1, 0,
                                  0, 0, 0, 1, 1, 1, 1, 0)
        self.ground.vertices = (-3, 0, -3, -2.5, 0, -3, -2.5, 0, -3.5, -3, 0, -3.5,
                                -2, 0, -3, -1.5, 0, -3, -1.5, 0, -3.5, -2, 0, -3.5,
                                -1, 0, -3, -0.5, 0, -3, -0.5, 0, -3.5, -1, 0, -3.5,
                                0.5, 0, -3, 1, 0, -3, 1, 0, -3.5, 0.5, 0, -3.5,
                                1.5, 0, -3, 2, 0, -3, 2, 0, -3.5, 1.5, 0, -3.5,
                                2.5, 0, -3, 3, 0, -3, 3, 0, -3.5, 2.5, 0, -3.5)
        current_y = 10
        self.lineheight = 30
        for ability in sorted(self.character.core.abilities, key=lambda a: a.current_cooldown):
            self.abilities_list.append((ability, pyglet.text.Label("{}: {}".format(ability.name, ability.current_cooldown), x=10, y=current_y, width=200, height=self.lineheight, batch=self.ability_labels)))
            current_y += self.lineheight
        

    def update(self, dt):
        # TODO: Add game logic for combat.
        for position in self.positions:
            for character in position:
                if character is not None:
                    character.update_combat(self, dt)

    def draw(self):
        self.game.set_view(self.game.PERSPECTIVE)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.gluLookAt(0, 2, 0, 0, 0, -4, 0, 1, 0)
        super().draw()
        self.game.set_view(self.game.ORTHO)
        # TODO: Draw other important information
        pyglet.gl.glLoadIdentity()
        self.ability_labels.draw()

    def on_mouse_release(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.RIGHT:
            self.game.restore_mode(self.last_mode)
        else:
            y -= 10
            for a in self.abilities_list:
                if y < self.lineheight:
                    break
                y -= self.lineheight
            else:
                return
            self.enemy.attack(a[0].attack)
            if self.enemy.dead:
                self.game.restore_mode(self.last_mode)

