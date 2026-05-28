from brain.parser import detect_intent
from brain.ai_brain import ask_ai

from voice.output import speak

from modules.system_control import (
open_app,
close_app,
minimize_app,
maximize_app,
play_pause,
next_song,
previous_song
)

from modules.web import (
play_song,
search_google,
get_info
)

from modules.automation import (
tell_time,
tell_date,
send_whatsapp_message
)

from gui.setup_gui import open_setup_gui

def extract_app_name(command, keywords):

    command = command.lower()

    if isinstance(keywords, str):
        keywords = [keywords]

    for word in keywords:
        command = command.replace(word, "")

    remove_words = ["please", "app", "application", "window"]

    for word in remove_words:
        command = command.replace(word, "")

    return command.strip()

def handle_command(command):

    intent = detect_intent(command)

    print("Intent:", intent)

    if "exit" in command or "stop" in command:

        speak("Goodbye")
        return

    elif "change your name" in command:

        speak("Opening profile settings")

        open_setup_gui()

        speak("Profile updated successfully")

    elif intent == "OPEN_APP":

        app_name = extract_app_name(command, "open")

        if app_name:

            speak(f"Opening {app_name}")

            open_app(app_name)

        else:

            speak("Which application should I open?")

    elif intent == "CLOSE_APP":

        app = extract_app_name(command, "close")

        result = close_app(app)

        speak(result)

    elif intent == "MAXIMIZE_APP":

        app = extract_app_name(command, "maximize")

        result = maximize_app(app)

        speak(result)

    elif intent == "MINIMIZE_APP":

        app = extract_app_name(
            command,
            ["minimize", "minimise", "minimixe"]
        )

        result = minimize_app(app)

        speak(result)

    elif intent == "NEXT_SONG":

        speak(next_song())

    elif intent == "PREVIOUS_SONG":

        speak(previous_song())

    elif intent == "PAUSE_SONG":

        speak(play_pause())

    elif intent == "PLAY_SONG":

        song = command.replace("play", "").strip()

        speak(f"Playing {song}")

        play_song(song)

    elif intent == "SEARCH_GOOGLE":

        query = command.replace("search", "").strip()

        speak(f"Searching {query}")

        search_google(query)

    elif intent == "GET_INFO":

        speak("Searching for information")

        result = get_info(command)

        speak(result)

    elif intent == "GET_TIME":

        current_time = tell_time()

        speak(f"The time is {current_time}")

    elif intent == "GET_DATE":

        current_date = tell_date()

        speak(f"Today is {current_date}")

    elif intent == "SEND_WHATSAPP_SMART":

        try:

            parts = command.split("to")

            message = parts[0]
            message = message.replace("send", "")
            message = message.replace("message", "")
            message = message.strip()

            name = parts[1].strip()

            speak(f"Sending message to {name}")

            result = send_whatsapp_message(name, message)

            speak(result)

        except Exception as e:

            print("ERROR:", e)

            speak("Sorry, I couldn't understand")

    else:

        speak("Let me think")

        response = ask_ai(command)

        speak(response)