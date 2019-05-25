from . import game

    
def main(first_mode):
    """Run the game."""
    g = game.Game()
    g.start_mode(first_mode)
    g.mainloop()
