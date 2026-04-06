import webbrowser
import time
import pyautogui
from modules.contacts import contacts
import datetime

def tell_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def tell_date():
    return datetime.datetime.now().strftime("%d %B %Y")

def set_reminder(seconds, message):
    time.sleep(seconds)
    return message

def send_whatsapp_message(name, message):
    name = name.lower()

    if name in contacts:
        number = contacts[name]

        # Open WhatsApp chat
        webbrowser.open(f"https://web.whatsapp.com/send?phone={number}")
        time.sleep(10)  # wait for WhatsApp to load

        # Type message
        pyautogui.write(message)
        time.sleep(1)
        pyautogui.press("enter")

        return "Message sent"
    else:
        return "Contact not found"