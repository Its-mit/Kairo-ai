# main.py


from voice.input import take_command
from voice.output import speak
from brain.parser import detect_intent
from modules.system_control import open_app, close_app, minimize_app, maximize_app, play_pause, next_song, previous_song
from modules.web import play_song, search_google, get_info
from modules.automation import tell_time, tell_date, set_reminder, send_whatsapp_message
from brain.ai_brain import ask_ai

import datetime

speak("Kai AI is starting")

def extract_app_name(command, keywords):
    command = command.lower()

    # Ensure keywords is a list
    if isinstance(keywords, str):
        keywords = [keywords]

    # Remove all keywords
    for word in keywords:
        if word in command:
            command = command.replace(word, "")

    # Remove filler words
    remove_words = ["please", "app", "application", "window"]
    for word in remove_words:
        command = command.replace(word, "")

    return command.strip()

while True:
    command = take_command()

    if not command:
        continue

    # Wake word check
    if "baby" not in command:
        continue

    # Remove wake word
    command = command.replace("baby", "").strip()

#   speak("Yes, I am listening")

    intent = detect_intent(command)
    print("Intent:", intent)

    #if intent == "GREETING":
    #    speak("Hey, I am Kairo AI. Ready to assist you.")


    

    if "exit" in command or "stop" in command:
        speak("Goodbye")
        break

    elif intent == "MAXIMIZE_APP":
        app = extract_app_name(command, "maximize")
        result = maximize_app(app)
        speak(result)

    elif intent == "MINIMIZE_APP":
        print("MINIMIZE COMMAND:", command)

        app = extract_app_name(command, ["minimize", "minimise", "minimixe"])
        print("EXTRACTED APP:", app)

        result = minimize_app(app)
        speak(result)

    elif intent == "CLOSE_APP":
        app = extract_app_name(command, "close")
        result = close_app(app)
        speak(result)   

    elif intent == "NEXT_SONG":
        result = next_song()
        speak(result)

    elif intent == "PREVIOUS_SONG":
        result = previous_song()
        speak(result)

    elif intent == "PAUSE_SONG":
        result = play_pause()
        speak(result)
        
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

    elif intent == "OPEN_APP":
        app_name = command.replace("open", "").strip()

        if app_name:
            speak(f"Opening {app_name}")
            open_app(app_name)
        else:
            speak("Which application should I open?")

    
    elif intent == "GET_TIME":
        current_time = tell_time()
        speak(f"The time is {current_time}")    

    elif intent == "GET_DATE":
        current_date = tell_date()
        speak(f"Today is {current_date}")

    elif intent == "SET_REMINDER":
        speak("In how many seconds?")
        sec = take_command()

        try:
            seconds = int(sec)
            speak("What should I remind you?")
            msg = take_command()

            speak(f"Reminder set for {seconds} seconds")
            reminder = set_reminder(seconds, msg)
            speak(reminder)

        except:
            speak("Invalid time")

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

        except:
            speak("Sorry, I couldn't understand")
    else:
        speak("Let me think")
        response = ask_ai(command)
        speak(response)