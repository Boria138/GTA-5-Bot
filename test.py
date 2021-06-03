import pyautogui
import keyboard
import pydirectinput
import time
from ahk import AHK

ahk = AHK()
win = ahk.find_window(title=b'Grand Theft Auto V')
win.activate()
win.maximize()
time.sleep(0.5)
while keyboard.is_pressed("Esc") == False:
    time.sleep(3)
    pydirectinput.press("w")
    pydirectinput.press("enter")
    print("Всё ok")
    time.sleep(0.01)
