# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random # Want to be choose a word at random
from words import words

"""
Get computer to choose a random word.
Check if word is valid for game use.
"""
def get_valid_word(words):
    word = random.choice(words) # Randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.lower() # Limit user input to lowercase

# print(get_valid_word(words))