import pyautogui
import keyboard
import os
import pydirectinput
import time
import mouse
files = os.listdir("Buttons")
while keyboard.is_pressed("Esc") == False:
    for f in files:
        picture = "Buttons/" + f
        time.sleep(3)
        button = pyautogui.locateOnScreen(picture, confidence=0.9)
        print(pyautogui.position())
        if button:
            print("Всё ок")
            mouse.move(433,551)w
            mouse.click()


        else:
            pydirectinput.press('w')
            print("Всё плохо")
            time.sleep(0.01)
