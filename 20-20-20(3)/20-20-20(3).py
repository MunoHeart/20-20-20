from tkinter import Tk
import tkinter as tk
from keyboard import press_and_release
from time import sleep

background_color = "#33334d" # one variable to make all changes when you wont to change the background color

class GUI():
    def __init__(self):
        # Define our quote window
        self.root = Tk()
        self.root.attributes('-fullscreen', True)  # to show a full screen window
        self.root.attributes('-alpha', 0.8)  # to make our window transparent
        self.root.configure(bg=background_color)  # background color
        self.quote_label = tk.Label(self.root, text="text", fg="orange", bg=background_color, justify="center", wraplength=600)
        self.quote_label.config(font=('times', 24, 'bold'))
        self.quote_label.pack(padx=None, pady=250) # position label at the middle
        self.show()


    def show(self):
        press_and_release("cmd + d")
        self.quotes_text()
        self.root.deiconify()
        # self.root.attributes('-topmost', 0)
        self.root.attributes('-topmost', 1)
        self.root.after(3000, self.hide) # duration: quote display >  "5000 (5 sec)"

    def hide(self):
        self.root.iconify() # hide the window
        sleep(30) # duration: Stretching and looking for a 6 feet object away form you > 30sec 
        self.notify()
        press_and_release("cmd + d")
        self.root.after(1200000, self.show) # duration: working > "1200000 (20 minutes)"


    def quotes_text(self):
        from random import choice
        quote_file = "E:\\Extension\\quotes_file.txt" # the quote file directory
        with open(quote_file, "r", encoding="utf8") as f:
            global random_quote
            random_quote = choice(f.readlines())
        self.quote_label['text'] = random_quote # to change the text in label to another random quote every time we call the function

    def notify(self):
        import winsound
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

if __name__ == '__main__':
    gui = GUI()
    gui.root.mainloop()