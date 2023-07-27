from tkinter import *
from tkinter import font
from info_window import get_info
from tkmacosx import Button
from wordle_class import Wordle
import string

def start_game():
    #Initialize window
    global window
    window = Tk()
    window.title("Wordle")

    #Initialize game
    game = Wordle()

    #Initialize welcome label
    welcome = Label(window, text = "Enter a five letter word below, click the info button for explanation of the rules.")
    welcome.grid(column=0, row=0, columnspan=5)

    #Initialize info button
    info = Button(window, text = "Info", command=get_info, bg='LightGrey')
    info.grid(column=5, row=0)

    #Initialize error message
    error = Label(window, text = "", fg='Black')
    orig_color = error.cget('background')
    error.grid(column=1, row=1, columnspan=3)

    #Remove error message function
    def exit_error():
        error['text'] = ""
        error.config(bg=orig_color)

    #Initialize wordle buttons
    line_1 = []
    line_2 = []
    line_3 = []
    line_4 = []
    line_5 = []
    lines = {
        0:line_1,
        1:line_2,
        2:line_3,
        3:line_4,
        4:line_5
    }

    for i in range(25):
        buttonFont = font.Font(size=20)
        button = Button(window, text = "", width=100, height=100, disabledbackground='White', disabledforeground='Black', font=buttonFont) 
        button.configure(state='disabled')
        if i < 5:
            line_1.append(button)
        elif i < 10:
            line_2.append(button)
        elif i < 15:
            line_3.append(button)
        elif i < 20:
            line_4.append(button)
        else:
            line_5.append(button)

    #Write into button function
    def write_button(key):
        letter = key.char
        if game.letter_number == 5:
            pass
        else:
            button = lines[game.attempts][game.letter_number]
            button.configure(state='normal')
            button['text'] = letter
            button.configure(state='disabled')
            game.letter_number += 1

    #Delete from button function
    def delete_button(arg=None):
        if game.letter_number == 0:
            pass
        else:
            game.letter_number -= 1
            button = lines[game.attempts][game.letter_number]
            button.configure(state='normal')
            button['text'] = ""
            button.configure(state='disabled')
    
    #Letter key binding
    alphabet = string.ascii_lowercase
    letter_bindings = []
    for letter in alphabet:
        i = window.bind(letter, write_button)
        letter_bindings.append(i)
    delete_ID = window.bind("<BackSpace>", delete_button)

    #place buttons
    for col in range(5):
        line_1[col].grid(column=col, row=2)
        line_2[col].grid(column=col, row=3)
        line_3[col].grid(column=col, row=4)
        line_4[col].grid(column=col, row=5)
        line_5[col].grid(column=col, row=6)

    #Entry and quit buttons
    def exit_window():
        window.destroy()
    retry = Button(window, text = "Retry", command=lambda: refresh())
    quit = Button(window, text = "Quit", command=exit_window)
    retry.grid(column=5, row=2)
    quit.grid(column=5, row=3)

    #Change button color function
    def change_color(button, color, letter):
        button.configure(state='normal')
        button['text'] = letter
        button.configure(disabledbackground=color)
        button.configure(state='disabled')

    #Entry function
    def take_input(arg=None):
        guess = ""
        for i in range(5):
            guess += lines[game.attempts][i]['text']
        if game.check_guess(guess):
            game.letter_number = 0
            index = 0
            for letter in guess:
                color = game.check_letter_of_guess(letter, index)
                change_color(lines[game.attempts][index], color, letter)
                index += 1
            if game.correct_word == guess:
                error.config(bg='White')
                error['text'] = "Congratualations you won!"
                i = 0
                for letter in alphabet:
                    window.unbind(letter, letter_bindings[i])
                    i+=1
                window.unbind("<BackSpace>", delete_ID)
                window.unbind("<Return>", enter_ID)
            elif not game.add_attempt():
                word = "The word was " + game.correct_word
                error['text'] = word
                error.config(bg='White')
                i = 0
                for letter in alphabet:
                    window.unbind(letter, letter_bindings[i])
                    i+=1
                window.unbind("<BackSpace>", delete_ID)
                window.unbind("<Return>", enter_ID)
            else:
                pass
        else:
            #Set error message
            error.config(bg='White')
            error['text'] = game.find_issue(guess)
            window.after(3000, exit_error)


    #Initialize entry
    enter_ID = window.bind("<Return>", take_input)

    #window loop
    window.mainloop()

if __name__ == '__main__':
    def refresh():
        window.destroy()
        start_game()
    
    start_game()