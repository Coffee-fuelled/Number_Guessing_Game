"""
File: testing.py

"""
import mock
from mock import patch
import pytest
from guess import Guess
from game import Game
from io import StringIO


def test_guess_correct(monkeypatch):
    """
    Test the guess for correct entry
    """
    guess = Guess(1, 100)
    monkeypatch.setattr('builtins.input', lambda _: "1")  # inputs 1 to guess
    result = guess.guess()
    assert result == 1


def test_game_1_guess(monkeypatch):
    game = Game(1, 100, 5)
    game.x = 25  # sets the number to 25
    monkeypatch.setattr('builtins.input', lambda _: "25")  # inputs 25 to game
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        game.play()
    assert mock_stdout.getvalue() == "\nCongratulations you did it in 1 goes\n"


def test_game_wrong_guess(monkeypatch):
    game = Game(1, 100, 5)
    game.x = 25  # sets the number to 25
    game.count = 4
    monkeypatch.setattr('builtins.input', lambda _: "26")  # inputs 25 to game
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        game.play()
    assert mock_stdout.getvalue() == "\nThe number is 25\n\nBetter Luck Next time!\n"


def test_game_correct_guess(monkeypatch):
    game = Game(1, 100, 5)
    game.x = 26  # sets the number to 26
    game.count = 4
    monkeypatch.setattr('builtins.input', lambda _: "26")  # inputs 25 to game
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        game.play()
    assert mock_stdout.getvalue() == "\nCongratulations you did it in 5 goes\n"


if __name__ == '__main__':
    pytest.main()
