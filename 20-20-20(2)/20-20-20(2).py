from tkinter import * 
import pyperclip


background_color = "#33334d" # one variable to make all changes when you wont to change the background color
# Define our quote window
root = Tk(className=" Quote Time")
root.attributes('-fullscreen', True)  # to show a full screen window
root.attributes('-alpha', 0.8)  # to make our window transparent
root.configure(bg=background_color)  # background color


# Extracting and preparing the quotes text from the quotes file
def quotes_text():
    from random import choice
    import os
    quote_file = os.getcwd() + "\\quotes_file.txt" # the quote file directory
    with open(quote_file, "r", encoding="utf8") as f:
        global random_quote
        random_quote = choice(f.readlines())
    quote_label['text'] = random_quote # to change the text in label to another random quote every time we call the function

# to skip the rest (that will not hide the windows that you working on) 
go_to_desktop = True
def wihou_going_to_desktop(event):
    global go_to_desktop
    go_to_desktop = False
    when_b_clicked(0)

# this what will happend when the you click ((b))
def when_b_clicked(event):
    from time import sleep
    from keyboard import press_and_release
    global go_to_desktop 

    root.withdraw()   # to hide the qoute window
    if go_to_desktop:
        press_and_release("cmd + d")
    quotes_text()
    if go_to_desktop:
        sleep(5)    # rest durations (20sec)
        play_sound()
        press_and_release("cmd + d")
    sleep(10)  # 20 minutes working
    root.deiconify()  # show the window

    go_to_desktop = True

def open_qoutes_file(event): # the event is what the bind keyboard shortcuts return
    import os
    os.startfile("E:/Extension/quotes_file.txt")

def copy_quote(event):
    pyperclip.copy(random_quote)

def copy_line_number(event):
    string_to_search = random_quote
    line_number = 0
    with open('E:/Extension/quotes_file.txt', "r", encoding="utf8") as f:
        # Read all lines in the file one by one
        for line in f:
            line_number += 1
            # For each line, check if line contains the string
            if string_to_search in line:
                pyperclip.copy(line_number)

def play_sound():
    import winsound
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)


quote_label = Label(root, text="text", fg="orange", bg=background_color, justify="center", wraplength=600)
quote_label.config(font=('times', 24, 'bold'))
quote_label.pack(padx=None, pady=250) # position label at the middle

root.bind('<b>', when_b_clicked) 
root.bind('<n>', wihou_going_to_desktop)
root.bind('<e>', open_qoutes_file)
root.bind('<c>', copy_quote)
root.bind('<l>', copy_line_number)



quotes_text()  # to display a quote at the first time before the quote_widget () open
root.mainloop()

