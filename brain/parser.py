def detect_intent(command):
    command = command.lower()

    if "open" in command:
        return "OPEN_APP"
    elif "send" in command and "to" in command:
        return "SEND_WHATSAPP_SMART"

    elif "play" in command:
        return "PLAY_SONG"

    elif "search" in command:
        return "SEARCH_GOOGLE"

    elif "who is" in command or "what is" in command:
        return "GET_INFO"

    elif "time" in command:
        return "GET_TIME"

    elif "hello" in command:
        return "GREETING"
    
    elif "date" in command:
        return "GET_DATE"

    elif "remind" in command:
        return "SET_REMINDER"

    elif "send message to" in command:
        return "SEND_WHATSAPP"
    
    else:
        return "AI"