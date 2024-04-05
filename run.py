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
def hangman():
    word = get_valid_word(words) # Variable stores valid letters
    word_letters = set(word) # Creates a new set of letters from chosen word
    aplphabet = set(string.ascii_lowercase)
    guessed_letters = set() # What the user has guessed
