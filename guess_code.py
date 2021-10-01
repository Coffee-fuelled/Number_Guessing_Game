"""
File: guess.py
Guessing a random number between the range of 1-100.
After each incorrect guess, ask user if they want a hint, if so..show hint.

MB -
Changed logic order so if 5th guess is correct it shows correctly
    did this by keeping the while count less than or equal to max guesses
    Then moving the if count to after the check for correct and making it greater than or equal
    to max guesses.
Added entry validation so won't error if a non number entered as a guess.
Also added remaining guesses after incorrect guess

"""

import random
# Initialise Variables
min_random = 1
max_random = 100
max_guesses = 5

# List of accepted hint requests.
hand = ['h', 'H']

# Generate random number.
x = random.randint(min_random, max_random)

# Initial number of guesses.
count = 0

print("\nYou've only " + str(max_guesses) + " chances to guess the number!\n")

# use less than so last guess counts
while count <= max_guesses:

    # Taking user input
    guess_in = input("Guess a number between " + str(min_random) + " and " + str(max_random) + ": ")

    try:
        # try to convert to int - except will catch error if not a number
        guess = int(guess_in)

        # increment count only when valid number guessed
        count += 1

        # Condition testing
        if x == guess:
            print("\nCongratulations you did it in " + str(count) + " goes")
            # Once guessed, loop will break
            break
        elif x != guess:
            # If Guessing is more than required guesses,shows this output.
            if count >= max_guesses:
                print("\nThe number is", x)
                print("\tBetter Luck Next time!")
                break
            else:
                # show remaining guesses, ask if hint wanted
                feedback = "Incorrect, " + str(max_guesses - count) + " guesses remaining, press H for a hint: "
                hint = str(input(feedback))
                # Check list against user input
                for i in hand:
                    if i in hint:
                        if x > guess:
                            print("You guessed too low!")
                        elif x < guess:
                            print("You Guessed too high!")
    # catches error if the guess is not a number
    except ValueError:
        print("Please enter a valid number! - Try again: ")

