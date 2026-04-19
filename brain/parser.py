# parsec

def detect_intent(command):
    command = command.lower()

    if any(word in command for word in ["open", "start", "launch"]):
        return "OPEN_APP"

    elif any(word in command for word in ["close", "exit", "quit"]):
        return "CLOSE_APP"

    elif any(word in command for word in ["minimize", "minimise", "minimixe"]):
        return "MINIMIZE_APP"
    elif any(word in command for word in ["maximize", "maximise", "full screen", "fullscreen"]):
        return "MAXIMIZE_APP"

    # -------- MUSIC CONTROL --------
    elif any(word in command for word in ["next"]):
        return "NEXT_SONG"

    elif any(word in command for word in ["previous", "back"]):
        return "PREVIOUS_SONG"

    elif any(word in command for word in ["pause", "stop song"]):
        return "PAUSE_SONG"

    elif "play" in command:
        return "PLAY_SONG"

    elif "send" in command and "to" in command:
        return "SEND_WHATSAPP_SMART"

    elif "search" in command:
        return "SEARCH_GOOGLE"

    elif "who is" in command or "what is" in command:
        return "GET_INFO"

    elif "time" in command:
        return "GET_TIME"

    elif "date" in command:
        return "GET_DATE"

    elif "remind" in command:
        return "SET_REMINDER"

    else:
        return "AI"