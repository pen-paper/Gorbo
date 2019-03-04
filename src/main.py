import sys
import game


def main(args):
    # TODO: Do any setup stuff, like loading things or logging in.
    main_game = game.Game()
    main_game.mainloop()
    # Save on exit?


if __name__ == "__main__":
    main(sys.argv)

