""""
File:       player.py
Author:     Matt Barton V244576
Description:
player class to save high scores

"""

from collections import namedtuple


class Player(object):
    """
    Player details for saving high scores
    """
    def __init__(self, _name, _score):
        self.name = _name
        self.score = _score

    def to_dict(self):
        return {"name": self.name, "score": self.score}


def from_dict(_dict):
    name = _dict.get('name')
    score = _dict.get('score')
    player = Player(name, score)
    return player
