# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random # Want to be choose a word at random
from words import words
import string


"""
Get computer to choose a random word.
Check if word is valid for game use - no spaces or dashes.
"""
def get_valid_word(words):
    word = random.choice(words) # Randomly chooses a word from the list
    """ Continues to iterate until no longer true. """
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.lower() # Limit user input to lowercase

# print(get_valid_word(words))


"""
Montior correctly guessed words.
Check letter validity.
"""
def gameplay():
    word = get_valid_word(words) # Variable stores valid letters
    word_letters = set(word) # Creates a new set of letters from word
    alphabet = set(string.ascii_lowercase)
    guessed_letters = set() # What the user has guessed

    lives = 9

    # Getting user input
    while len(word_letters) > 0 and lives > 0: # Iterate over until conditions are met

        # Letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f"You have {lives} left.\n")
        print(f"You have used these letters: {' '.join(guessed_letters)}.\n")

        # Current word is... (ie W - R D)
        # Displays guessed letters
        current_word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print(f"Current word: {' '.join(current_word_list)}.\n")

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                # word_letter decreases with each correct guess
                word_letters.remove(user_letter)#
            else:
                lives = lives - 1 # Takes away a life if wrong
                print("That letter is not in the word.\n")


        elif user_letter in guessed_letters:
            print("You have already used that letter. Please try again.\n")

        else:
            print("Invalid letter. Please try again.\n")

    # While condition gets here when condition is met aka len(word_letters) == 0
    if lives == 0:
        print(f"Sorry, you died! The word was {word}.\n")
    else:
        print(f"Congratulations! You guessed the word, {word}!\n")



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

    elif user_letter in guessed_letters: # Invalid guess; already tried
        print("You have already used that letter. Please try again.\n")
    else:
        print("Invalid letter. Please try again.\n") # Invalid input


gameplay()
user_input = input("Type something:")
print(user_input)
