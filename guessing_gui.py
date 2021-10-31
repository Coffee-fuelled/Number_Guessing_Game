"""
File: guessing_gui.py
Sets up the Graphical user interface for the guessing game
"""
from breezypythongui import EasyFrame
import random
from hint import Hint
from guess import Guess
import scoring
from player import Player


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
        self.guess_in = 0
        self.message = ""
        self.the_letters = ""
        self.guess = Guess(self.min_range, self.max_range)
        self.high_score = 0
        self.high_score_name = ""

        super().__init__(title="Guessing Game", width=500, height=350, background="light blue")

        high_score_player = scoring.get_high_score()
        self.high_score = high_score_player.score
        self.high_score_name = high_score_player.name

        self.Title = self.addLabel(text="Guess a number between " + str(self.min_range) +
                                        " and " + str(self.max_range) + ": ",
                                   row=0, column=0, columnspan=8, sticky="EW", font="Verdana",
                                   foreground="#ffffff",
                                   background="navy")
        self.GuessLabel = self.addLabel(text="What is Your Guess?",
                                        row=1, column=0, sticky="NS", foreground="#090909", background="light blue")
        self.NumberGuessed = self.addIntegerField(value=0, row=1, column=1,sticky="NSEW")
        self.GuessButton = self.addButton(text="Guess!",
                                          row=1, column=3, columnspan=4, command=self.check_guess)
        self.HintButton = self.addButton(text="Hint!", row=3, column=4, columnspan=4,
                                         command=self.check_hint, state="disabled")
        self.ReplayButton = self.addButton(text="Play Again?", row=3, column=0, columnspan=3,
                                           command=self.play_again, state="disabled")
        self.QuitButton = self.addButton(text="Quit", row=3, column=2, command=self.quit)
        self.MessageLabel = self.addLabel(text="Take a Guess...",
                                          row=2, column=0, columnspan=3, sticky="NSEW", background="light blue")
        self.GuessCount = self.addLabel(text="0 Guesses used", row=2, column=4, sticky="W")
        self.hint = Hint(self.MessageLabel)
        # new scoring attributes here
        self.player_name_label = self.addLabel(text="High Score By ", row=4, column=0, columnspan=3, sticky="E",
                                               background="light blue")
        self.player_name = self.addTextField(text="", row=5, column=0, columnspan=3, sticky="E", state="disabled")
        self.player_high_score_label = self.addLabel(text="High Score", row=4, column=4, columnspan=2, sticky="E",
                                                     background="light blue")
        self.player_high_score = self.addIntegerField(value=0, row=5, column=4, columnspan=2, sticky="E",
                                                      state="disabled")
        self.current_score_label = self.addLabel(text="Current Score", row=4, column=6, columnspan=2, sticky="E",
                                                 background="light blue")
        self.player_score = self.addIntegerField(value=0, row=5, column=6, columnspan=2, sticky="E", state="disabled")
        self.save_button = self.addButton(text="Save Score", row=6, column=4, columnspan=3,
                                          command=self.save_score, state="disabled")
        self.save_messages = self.addLabel(text="", row=6, column=0, columnspan=3, sticky="E",
                                           background="light blue")
        self.player_high_score.setValue(self.high_score)
        self.player_name.setText(self.high_score_name)
        # command handling methods after this

    def check_guess(self):
        self.guess_in = self.guess.check_guess(self.x, self.max_guesses, self.NumberGuessed, self.MessageLabel,
                                               self.HintButton, self.GuessButton, self. ReplayButton, self.GuessCount,
                                               self.player_score, self.save_button, self.player_name)

    def check_hint(self):

        self.hint.get_hint(self.guess_in, self.x)

    def play_again(self):
        self.count = 0
        self.x = random.randint(self.min_range, self.max_range)
        self.GuessCount["text"] = str(self.count)+" Guesses used"
        self.NumberGuessed.setNumber(0)
        changeTextColour(self.MessageLabel, "Take a Guess...", "black", "white")
        self.GuessButton["state"] = "normal"
        self.guess = Guess(self.min_range, self.max_range)
        self.save_button['state'] = "disabled"
        self.save_messages['text'] = ""
        # section added for scoring handling
        # recall get high score
        high_score_player = scoring.get_high_score()
        # set the score name and score to the variables
        self.high_score = high_score_player.score
        self.high_score_name = high_score_player.name
        # update the frame with the score details
        self.player_high_score.setValue(self.high_score)
        self.player_name.setText(self.high_score_name)
        # disable the save button and name fields
        self.ReplayButton["state"] = "disabled"
        self.player_name["state"] = "disabled"

    def handle_hint_button(self):
        self.HintButton["state"] = "disabled"

    def save_score(self):
        # get the score from the count field
        score = self.player_score.getNumber()
        # call the save score function
        scoring.save_high_score(self.player_name.get(), score, self.save_messages, self.save_button,
                                self.player_name)


def changeTextColour(att, message, fore, back):
    att["text"] = message
    att["foreground"] = fore
    att["background"] = back
