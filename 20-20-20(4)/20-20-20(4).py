# "Take a Break" Notification system in Python
import time
from random import choice

import keyboard
from win10toast import ToastNotifier

n = ToastNotifier()


def notifyMe(title, body, duration):

    n.show_toast(
        title=title,
        msg=body,
        icon_path="E:\\Extension\\alarm.ico",
        duration=duration,
    )

def quotes_text():
        quote_file = "E:\\Extension\\quotes_file.txt" # the quote file directory
        with open(quote_file, "r", encoding="utf8") as f:
            random_quote = choice(f.readlines())
        return random_quote

if __name__ == '__main__':
    while True:
        time.sleep(1200) # 1200 sec = 20 min. (work time)
        # keyboard.press_and_release("cmd + d")
        notifyMe(quotes_text(), ".", 25) #25 sec (rest time)
        # keyboard.press_and_release("cmd + d")
        notifyMe("!!! 20-20-20 !!!", "Go Back", 5)
