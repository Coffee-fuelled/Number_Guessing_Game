"""
File: guess.py
Guess object - handles guess inputs
"""


class Guess(object):
    """
    Handles guess input and validates the guess
    """
    def __init__(self, min_random, max_random):
        # min and max to allow for message to user
        self.min = min_random
        self.max = max_random
        self.guess_string = "Guess a number between " + str(self.min) + " and " + str(self.max) + ": "
        self.out_of_range_string = "Number must be " + str(self.min) + " - " + str(self.max) + " - Please try again!"
        self.nan_string = "Enter a valid number! - Please try again: "

        self.run = True
    def guess(self):
        """
        Asks the player for a guess
        Validates the answer is within the valid range
        Validates is a number
        :return: valid guess
        """

        while self.run:  # use while loop to continue until a correct entry is given
            entry = (input(self.guess_string))  # ask for move
            try:
                move = int(entry)  # try to convert entry to an int
                if move < self.min or move > self.max:
                    print(self.out_of_range_string)  # input out of range try again
                else:
                    break  # entry is an int within range so break the while loop
            except ValueError:  # if a value error then incorrect format
                print(self.nan_string)
        return move