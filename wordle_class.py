from random_word_list import dictionary
from random_word_list import full_word_list
import random

class Wordle():
    def __init__(self):
        self.correct_word = random.choice(dictionary)
        self.attempts = 0
        self.letter_number = 0
    
    def check_guess(self, guess):
        if len(guess) != 5:
            return False
        elif guess not in full_word_list:
            return False
        else:
            return True
    
    def find_issue(self, guess):
        if len(guess) != 5:
            return "Please choose a 5 letter word"
        elif guess not in full_word_list:
            return "Not in word list"
        else:
            return "nothing"
    
    def check_letter_of_guess(self, letter, index):
        if letter in self.correct_word:
            if self.correct_word[index] == letter:
                return 'Green'
            else:
                return 'Yellow'
        else:
            return 'Red'
    
    def add_attempt(self):
        self.attempts += 1
        if self.attempts == 5:
            return False
        else:
            return True
    

