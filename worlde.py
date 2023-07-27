import os
os.system('cls' if os.name == 'nt' else 'clear')

from turtle import clear
from random_word_list import dictionary
import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
green_checked = []
yellow_checked = []
red_checked = []

correct = random.choice(dictionary).lower()
guess = ""

yellow = "\033[33m"
green = "\033[32m"
red = "\033[31m"
reset = "\033[0m"

gave_up = False
loser = False
me = False

counter = 0

class InputError(Exception):
    pass


print("Welcome to scuffed wordle (type exit to give up)")
print("Guess the 5 letter word below.")

while guess != correct:
    try:
        print("|||||", end = "\t")
        for i in range(13):
            print(alphabet[i], end = " ")
        print("")
        print("VVVVV", end = "\t")
        for i in range(13, 26):
            print(alphabet[i], end = " ")
        print("")
        guess = input()
        if guess == "exit":
            loser = True
            break
        elif guess == "out":
            me = True
            break
        elif len(guess) != 5:
            print("Please enter a five letter word.")
            raise InputError
        elif guess not in dictionary:
            print(guess + " is not in the word list.")
            raise InputError  
        for i in guess:
            if i in correct:
                if correct.index(i) == guess.index(i):
                    if i in green_checked and i in yellow_checked:
                        print(green + i + reset, end = "")
                        continue
                    elif i in yellow_checked:
                        index = alphabet.index(yellow + i + reset)
                        alphabet[index] = green + i + reset
                        green_checked.append(i)
                    else:
                        index = alphabet.index(i)
                        alphabet[index] = green + i + reset
                        green_checked.append(i)
                        yellow_checked.append(i)
                    print(green + i + reset, end = "")
                else:
                    if i not in yellow_checked and i not in green_checked:
                        index = alphabet.index(i)
                        alphabet[index] = yellow + i + reset
                        yellow_checked.append(i)
                    print(yellow + i + reset, end = "")
            else:
                if i not in red_checked: 
                    index = alphabet.index(i)
                    alphabet[index] = red + i + reset
                print(i, end = "")
            red_checked.append(i)
        print("")
        counter += 1
        if counter == 5:
            loser = True
            break
    except InputError:
        continue

if gave_up:
    print ("Imagine giving up, pretty trash lmao. You don't even deserve to know the word.")
elif loser:
    print("Damn you lost, couldn't even figure out a 5 letter word. You don't even deserve to know this word, try again with a different one.")
else:
    if not me:
        counter = str(counter)
        print("Congratulations the word was " + green + correct + reset + " it took you " + counter + " guesses")
    else:
        print(correct)