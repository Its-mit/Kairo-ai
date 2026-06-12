# main.py
from voice.input import take_command
from voice.output import speak

from brain.personality import get_wake_word
from brain.command_router import handle_command

from memory import load_profile
from gui.setup_gui import open_setup_gui

# -------- FIRST TIME SETUP --------

profile = load_profile()

if profile is None:

    speak("Hello I am KAIRO AI your personal AI assistant")

    speak("Please enter your details")

    open_setup_gui()

    profile = load_profile()

    speak(f"Nice to meet you {profile['name']}")

else:

    speak("System initialized successfully")

    speak(f"Welcome back {profile['name']}")

# -------- MAIN LOOP --------

while True:

    command = take_command()

    if not command:
        continue

    wake_word = get_wake_word().lower()

    if wake_word not in command:
        continue

    command = command.replace(wake_word, "").strip()

    if not command:
        speak("Yes {greeting}")
        continue

    handle_command(command)
