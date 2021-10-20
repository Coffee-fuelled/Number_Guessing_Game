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
        self.guess = 0
        self.count = 0

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

    def check_guess(self, x, max_guesses,  att_number_guessed, att_message_label, att_hint_button,
                    att_guess_button, att_replay_button, att_guess_count):
        """
        """

        try:
            self.guess = att_number_guessed.getNumber()
            if self.guess < self.min or self.guess > self.max:
                changeTextColour(att_message_label, f"Number must be " + str(self.min)
                                 + " - " + str(self.max) + " - Please try again!", "white", "red")
            else:
                att_hint_button["state"] = "normal"
                self.count += 1
                if self.guess == x:
                    changeTextColour(att_message_label, f"You got it in {self.count} guesses!", "white", "green")
                    att_guess_button["state"] = "disabled"
                    att_hint_button["state"] = "disabled"
                    att_replay_button["state"] = "normal"
                else:
                    if self.count >= max_guesses:
                        changeTextColour(att_message_label, f"The number is {x},"
                                                            f" Better Luck Next time!", "white", "orange")
                        att_guess_button["state"] = "disabled"
                        att_hint_button["state"] = "disabled"
                        att_replay_button["state"] = "normal"
                    else:
                        changeTextColour(att_message_label,
                                         f"Not Correct - Click the button for a hint!", "white", "orange")

        except ValueError:
            changeTextColour(att_message_label, "You need to enter an integer!",  "red", "white")

        finally:
            att_guess_count["text"] = str(self.count + 1)+" Guesses"
        # end of check guess*******
        return self.guess


def changeTextColour(att, message, fore, back):
    att["text"] = message
    att["foreground"] = fore
    att["background"] = back
