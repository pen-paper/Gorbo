from . import game

    
def main(first_mode):
    g = game.Game()
    g.start_mode(first_mode)
    g.mainloop()
