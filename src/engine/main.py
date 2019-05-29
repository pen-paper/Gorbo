from . import game

    
def main(game_file):
    """Run the game."""
    g = game.Game(game_file)
    g.mainloop()
