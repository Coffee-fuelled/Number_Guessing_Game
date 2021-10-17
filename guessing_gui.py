"""
File: guessing_gui.py

Sets up the Graphical user interface for the guessing game

"""

from breezypythongui import EasyFrame
import string
import csv
import random
from hint import Hint
from guess import Guess



class GuessingGame(EasyFrame):

    """Guessing Game Class"""
    def __init__(self, min_random, max_random, max_guess_count):

        """ Initialise the frame and instance variables"""
        self.count = 0
        self.min_range = min_random
        self.max_range = max_random
        self.x = random.randint(self.min_range, self.max_range)
        self.max_guesses = max_guess_count
        self.guess_in = 0
        self.message = ""
        self.the_letters = ""
        self.guess = Guess(self.min_range, self.max_range)
        self.guess = 0
        self.message = ""
        self.the_letters = ""


        super().__init__(title="Guessing Game", width=500, height=350)

        self.Title = self.addLabel(text="Guess a number between " + str(self.min_range) +
                                        " and " + str(self.max_range) + ": ",
                                   row=0, column=0, columnspan=3, sticky="EW", font="Verdana",
                                   foreground="#ffffff",
                                   background="#000000")

        self.GuessLabel = self.addLabel(text="What is Your Guess?",
                                        row=1, column=0, foreground="#090909")

        self.NumberGuessed = self.addIntegerField(value=0, row=1, column=1)

        self.GuessButton = self.addButton(text="Guess!",
                                          row=2, column=3, columnspan=3, command=self.check_guess)

        self.HintButton = self.addButton(text="Hint!", row=3, column=2, columnspan=3,
                                         command=self.check_hint, state="disabled")

        self.ReplayButton = self.addButton(text="Play Again?", row=4, column=0, columnspan=3,
                                           command=self.play_again, state="disabled")

        self.QuitButton = self.addButton(text="Quit", row=4, column=2, command=self.quit)

        self.MessageLabel = self.addLabel(text="Take a Guess...",
                                          row=2, column=0, columnspan=3, sticky="NSEW")

        self.GuessCount = self.addLabel(text="1 Guess", row=4, column=0)

        self.hint = Hint(self.MessageLabel)

        # command handling methods after this

    def check_guess(self):
        self.guess_in = self.guess.check_guess(self.x, self.max_guesses, self.NumberGuessed, self.MessageLabel, self.HintButton,
                                               self.GuessButton, self. ReplayButton, self.GuessCount)

        # end of check guess*******

    def handle_hint_button(self):
        self.HintButton["state"] = "disabled"


def changeTextColour(att, message, fore, back):
    att["text"] = message
    att["foreground"] = fore
    att["background"] = back


def main():
    GuessingGame(1, 100, 5).mainloop()


if __name__ == "__main__":
    main()
