import pyautogui
import keyboard
import os
import pydirectinput
import time
from ahk import AHK

ahk = AHK()
win = ahk.find_window(title=b'Grand Theft Auto V')
win.activate()
win.maximize()
time.sleep(0.5)
files = os.listdir("Buttons")
while keyboard.is_pressed("Esc") == False:
    time.sleep(3)
    for f in files:
        picture = "Buttons/" + f
        button = pyautogui.locateOnScreen(picture, confidence=0.9)
        time.sleep(0.02)
        if button:
            print("Всё ок")
            pyautogui.click(button)
            time.sleep(0.01)
    else:

        pydirectinput.press("w")
        time.sleep(3)
        pydirectinput.press("enter")
        print("Всё плохо")
        time.sleep(0.01)
