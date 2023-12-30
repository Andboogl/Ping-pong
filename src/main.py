"""Main module. Runs game"""


from game import Game


def main() -> None:
    """Runs game"""
    game = Game()
    game.mainloop()


if __name__ == '__main__':
    main()
