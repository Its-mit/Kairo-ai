#system_control


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
    "chrome": "Chrome"
}


def get_window(app_name):
    import pygetwindow as gw

    app_name = APP_ALIASES.get(app_name, app_name)
    app_name = app_name.lower()

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
        win.activate()
        win.maximize()
        return f"{app_name} maximized"
    return "App not found"

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

            return f"{app_name} minimized"
        except Exception as e:
            print("ERROR:", e)
            return "Failed to minimize"
    return "App not found"

# -------- CLOSE --------
def close_app(app_name):
    win = get_window(app_name)
    if win:
        win.activate()
        win.close()
        return f"{app_name} closed"
    else:
        # fallback (old method)
        os.system(f"taskkill /f /im {app_name}.exe")
        return f"{app_name} closed"
    




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