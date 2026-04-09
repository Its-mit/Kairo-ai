import webbrowser
import time
import pyautogui
from modules.contacts import contacts
import datetime
import urllib.parse

def tell_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def tell_date():
    return datetime.datetime.now().strftime("%d %B %Y")

def set_reminder(seconds, message):
    time.sleep(seconds)
    return message

def send_whatsapp_message(name, message):
    try:
        number = contacts.get(name.lower())

        if not number:
            return "Contact not found"

        msg = urllib.parse.quote(message)
        url = f"https://web.whatsapp.com/send?phone={number}&text={msg}"

        webbrowser.open(url)
        time.sleep(15)
        pyautogui.press("enter")

        return "Message sent successfully"

    except Exception as e:
        print("ERROR:", e)
        return "Failed"