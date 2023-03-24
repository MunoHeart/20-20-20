# "Take a Break" Notification system in Python
import time
import keyboard
from win10toast import ToastNotifier
n = ToastNotifier()


def notifyMe(title, body, duration):

    n.show_toast(
        title=title,
        msg=body,
        icon_path="E:/Extention/alarm.ico",
        duration=duration
    )


if __name__ == '__main__':
    while True:
        time.sleep(1200)
        keyboard.press_and_release("cmd + d")
        notifyMe("!!! 20-20-20 !!!", "Jump Up", 25)
        keyboard.press_and_release("cmd + d")
        notifyMe("20-20-20.py!! 20-20-20 !!!", "Go Back", 25)
