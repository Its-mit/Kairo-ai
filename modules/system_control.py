#system_control.py

import pygetwindow as gw
import pyautogui
import time
import os

# -------- FIND WINDOW --------
APP_ALIASES = {
    "vs code": "Visual Studio Code",
    "visual studio code": "Visual Studio Code",
    "code": "Visual Studio Code",
    "brave": "Brave",
    "chrome": "Chrome",
    "word": "Word",
    "excel": "Excel",
    "notepad": "Notepad"
}

def get_window(app_name):
    # If the AI tells us the target is the current window, grab the active one
    if not app_name or app_name.lower() in ["current", "this", "window", "it", "default"]:
        try:
            return gw.getActiveWindow()
        except:
            pass

    app_name = APP_ALIASES.get(app_name.lower(), app_name).lower()

    for title in gw.getAllTitles():
        if app_name in title.lower() and title.strip():
            return gw.getWindowsWithTitle(title)[0]

    return None

# ---------------- OPEN APP ----------------
def open_app(app_name):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write(app_name)
    time.sleep(1)
    pyautogui.press('enter')

# -------- MAXIMIZE --------
def maximize_app(app_name):
    win = get_window(app_name)
    if win:
        try:
            win.activate()
            win.maximize()
            return f"Maximized"
        except:
            return "Failed to maximize."
    return "App not found on screen"

# -------- MINIMIZE --------
def minimize_app(app_name):
    win = get_window(app_name)
    if win:
        try:
            win.activate()
            time.sleep(0.3)
            # press twice to fully minimize
            pyautogui.hotkey('win', 'down')
            time.sleep(0.2)
            pyautogui.hotkey('win', 'down')
            return f"Minimized"
        except Exception as e:
            print("ERROR:", e)
            return "Failed to minimize"
    return "App not found on screen"

# -------- CLOSE --------
def close_app(app_name):
    win = get_window(app_name)
    if win:
        try:
            win.activate()
            win.close()
            return f"Closed"
        except:
            pass
    
    # fallback (old method) if window isn't found cleanly
    if app_name.lower() not in ["current", "this", "window"]:
        os.system(f"taskkill /f /im {app_name}.exe")
        return f"{app_name} closed via terminal"
    
    return "Could not close."

# ---------------- MUSIC CONTROL ----------------
def play_pause():
    pyautogui.press("playpause")
    return "Toggled play"

def next_song():
    pyautogui.press("nexttrack")
    return "Next song"

def previous_song():
    pyautogui.press("prevtrack")
    return "Previous song"