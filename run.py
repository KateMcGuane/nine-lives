import random  # Want to be choose a word at random
from words import words
import string


"""
*GAME LOGIC*
Credit:
https://www.youtube.com/watch?v=8ext9G7xspg&t=5795s&ab_channel=freeCodeCamp.org

Get computer to choose a random word.
Check if word is valid for game use - no spaces or dashes.
"""


def get_valid_word(words):
    word = random.choice(words)  # Randomly chooses a word from the list
    """ Continues to iterate until no longer true. """
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.lower()  # Limit user input to lowercase


"""
Montior correctly guessed words.
Check letter validity.
"""


def gameplay():
    word = get_valid_word(words)  # Variable stores valid letters
    word_letters = set(word)  # Creates a new set of letters from word
    alphabet = set(string.ascii_lowercase)
    guessed_letters = set()  # What the user has guessed

    lives = 9

    # Getting user input
    # Iterate over until conditions are met
    while len(word_letters) > 0 and lives > 0:

        # Letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f"\nYou have {lives} lives left.")
        print(f"\nYou have tried: {' '.join(guessed_letters)}")

        # Current word is... (ie W - R D)
        # Displays guessed letters
        current_word_list =
        [letter if letter in guessed_letters else '-' for letter in word]
        print(f"\nCurrent word: {' '.join(current_word_list)}")

        user_letter = input("\nGuess a letter: ").lower()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                # word_letter decreases with each correct guess
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # Takes away a life if wrong
                print("\nThat letter is not in the word.")

        elif user_letter in guessed_letters:
            print("\nYou have already used that letter. Please try again.")

        else:
            print("\nInvalid character. Please try again.")

    # While condition gets here when condition is met -- len(word_letters) == 0
    if lives == 0:
        print(f"\nSorry, you died! The word was {word}.")
    else:
        print(f"\nCongratulations! You guessed the word, {word}!")

    """
    If this is a valid character in the alphabet not yet used,
    add this to guessed_letters set.
    If the letter guessed is in the word, remove that letter
    from word_letters.
    """

    if user_letter in alphabet - guessed_letters:
        guessed_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in guessed_letters:  # Invalid guess; already tried
        print("\nYou have already used that letter. Please try again.")
    else:
        print("\nInvalid letter. Please try again.")  # Invalid input


gameplay()
user_input = input("Type something: \n")
print(user_input)