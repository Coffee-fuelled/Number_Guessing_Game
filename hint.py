"""
Filename: hint.py
"""


class Hint(object):

    def __init__(self, att):
        self.att = att

    def get_hint(self, guess, number):
        """
        """
        if guess < number:
            changeTextColour(self.att, f"Too Low", "white", "red")
        elif guess > number:
            changeTextColour(self.att, f"Too High", "white", "blue")


def changeTextColour(att, message, fore, back):
    att["text"] = message
    att["foreground"] = fore
    att["background"] = back