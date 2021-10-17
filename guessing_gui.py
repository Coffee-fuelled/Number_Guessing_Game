"""
File: guessing_gui.py
Sets up the Graphical user interface for the guessing game
"""

from breezypythongui import EasyFrame
import string
import csv
import random
from hint import Hint



class GuessingGame(EasyFrame):

    """Guessing Game Class"""
    def __init__(self, min_random, max_random, max_guess_count):

        """ Initialise the frame and instance variables"""
        self.count = 0
        self.min_range = min_random
        self.max_range = max_random
        self.x = random.randint(self.min_range, self.max_range)
        self.max_guesses = max_guess_count
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

        """
        """
        try:
            self.guess = self.NumberGuessed.getNumber()
            if self.guess < self.min_range or self.guess > self.max_range:
                changeTextColour(self.MessageLabel, f"Number must be " + str(self.min_range)
                                 + " - " + str(self.max_range) + " - Please try again!", "white", "red")
            else:
                self.HintButton["state"] = "normal"
                self.count += 1
                if self.guess == self.x:
                    changeTextColour(self.MessageLabel, f"You got it in {self.count} guesses!", "white", "green")
                    self.GuessButton["state"] = "disabled"
                    self.HintButton["state"] = "disabled"
                    self.ReplayButton["state"] = "normal"
                else:
                    if self.count >= self.max_guesses:
                        changeTextColour(self.MessageLabel, f"The number is {self.x},"
                                                            f" Better Luck Next time!", "white", "orange")
                        self.GuessButton["state"] = "disabled"
                        self.HintButton["state"] = "disabled"
                        self.ReplayButton["state"] = "normal"
                    else:
                        changeTextColour(self.MessageLabel,
                                         f"Not Correct - Click the button for a hint!", "white", "orange")

        except ValueError:
            changeTextColour(self.MessageLabel, "You need to enter an integer!",  "red", "white")

        finally:
            self.GuessCount["text"] = str(self.count + 1)+" Guesses"

    def check_hint(self):
        """
        """
        self.hint.get_hint(self.guess, self.x)

    def play_again(self):
        self.count = 0
        self.x = random.randint(self.min_range, self.max_range)
        self.GuessCount["text"] = str(self.count + 1)
        self.NumberGuessed.setNumber(0)
        changeTextColour(self.MessageLabel, "Take a Guess...", "black", "white")
        self.GuessButton["state"] = "normal"

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
