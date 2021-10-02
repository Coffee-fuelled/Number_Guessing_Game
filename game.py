"""
File: game.py

Game object for Guessing Game

"""
# imports
import random
from guess import Guess


class Game (object):
    """
    Game class for Guessing game
    """
    def __init__(self, min_random, max_random, max_guess_count):

        # Generate random number.
        self.x = random.randint(min_random, max_random)

        self.min_range = min_random
        self.max_range = max_random
        self.max_guesses = max_guess_count
        self.hand = ['h', 'H']  # accepted inputs for hint request
        # Guess class
        self.guess = Guess(min_random, max_random)
        self.count = 0

    def play(self):
        """
        Puts it all together
        :return:
        """

        while self.count <= self.max_guesses:
            #  guess from player
            guess_in = self.guess.guess()
            # once valid guess increment count
            self.count += 1
            # check guess against random number
            if self.x == guess_in:
                print("\nCongratulations you did it in " + str(self.count) + " goes")
                # Once guessed, loop will break
                break
            else:
                if self.count >= self.max_guesses:
                    print("\nThe number is", self.x)
                    print("\nBetter Luck Next time!")
                    break
                else:
                    hint = self.hint(self.count, guess_in)
                    print(hint)
        # return true = game over so calling code knows if game is playing or over
        return True

    def hint(self, count, guess):
        """
        Checks if the player wants a hint
        if they select H or h for hint then returns if guess is high or lower.
        :return: Hint
        """
        feedback = ""  # no feed back if entry is not h or H so blank string returned in that case
        hint = str(input("Incorrect, " + str(self.max_guesses - count) + " guesses remaining, press H for a hint: "))
        for i in self.hand:
            if i in hint:
                if self.x > guess:
                    feedback = "You guessed too low!"
                elif self.x < guess:
                    feedback = "You Guessed too high!"
        return feedback
