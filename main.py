"""
File:  main.py

Main guessing game code to put it all together

"""

from game import Game


def main():
    """


    """
    # Initialise Variables
    min_random = 1
    max_random = 100
    max_guesses = 5
    # Sample results for play again
    again = ['y', 'Y']

    # Start the game
    print("\nWelcome to Guessing Game!")
    print("\nYou've only " + str(max_guesses) + " chances to guess the number!\n")

    # set playing to true to allow for replay
    playing = True

    while playing:
        # initialise Game
        game = Game(min_random, max_random, max_guesses)

        if game.play():
            print("Do you want to play another game?")
            play_again = input("Press y to play again: ")
            if play_again in again:
                print("Excellent - we are playing again!")
                playing = True
            else:
                playing = False
                print("Bye please play again some time!")


if __name__ == '__main__':
    main()
