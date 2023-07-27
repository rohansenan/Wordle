from tkinter import *

#Info Button Function
def get_info():
    #Initialize info window
    info_window = Tk()
    info_window.title("Info")
    info_window.geometry("717x318")

    #Initialize labels
    intro = Label(info_window, text = "Below are the rules of the game:")
    green = Label(info_window, text = "Green", fg='Green')
    green_info = Label(info_window, text = "= The letter is in the word and in that spot")
    yellow = Label(info_window, text = "Yellow", fg='Yellow')
    yellow_info = Label(info_window, text = "= The letter is in the word but not in that spot")
    red = Label(info_window, text = "Red", fg='Red')
    red_info = Label(info_window, text = "= The letter is not in the word")
    note = Label(info_window, text = "Note that while it may be a real word, if it is not within the word list \
(list of possible words) it will not be a valid guess")

    #Ok button action
    def exit_info(arg=None):
        info_window.destroy()

    #Initialize ok button
    ok = Button(info_window, text = "Ok", command=exit_info)

    #Set label and button positions
    intro.place(relx=0, rely=0)
    green.place(relx=0, rely=0.2)
    green_info.place(relx=0.057, rely=0.2)
    yellow.place(relx=0, rely=0.4)
    yellow_info.place(relx=0.062, rely=0.4)
    red.place(relx=0, rely=0.6)
    red_info.place(relx=0.04, rely=0.6)
    note.place(relx=0, rely=0.8)
    ok.place(relx=0, rely=0.9, relwidth=1)

    #Key bindings
    info_window.bind("<Return>", exit_info)