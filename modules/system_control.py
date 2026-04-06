import pyautogui
import time

def open_app(app_name):
    # Open start menu
    pyautogui.press('win')
    time.sleep(1)

    # Type app name
    pyautogui.write(app_name)
    time.sleep(1)

    # Press enter
    pyautogui.press('enter')