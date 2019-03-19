import sys
from src import game
from src.modes import main_menu


def main(args):
    # TODO: Do any setup stuff, like loading things or logging in.
    main_game = game.Game()
    m = main_menu.MainMenu()
    main_game.start_mode(m)
    main_game.mainloop()
    # Save on exit?


if __name__ == "__main__":
    main(sys.argv)

