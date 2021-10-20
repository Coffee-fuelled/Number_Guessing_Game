"""
File:  main.py
Main guessing game code to put it all together
"""

from guessing_gui import GuessingGame


def main():
    """
    """
    GuessingGame(1, 100, 5).mainloop()


if __name__ == '__main__':
    main()
