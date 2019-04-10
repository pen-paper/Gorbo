from ..engine import Mode, NullController, ORTHOGONAL

from .menu_sprite import MenuSprite


class TestMenu(Mode):
    def __init__(self):
        super().__init__()
        self.sprites.append(MenuSprite(NullController, self, None))

    def setup(self, game, last_mode):
        super().setup(game, last_mode)
        self.game.set_view(ORTHOGONAL)
