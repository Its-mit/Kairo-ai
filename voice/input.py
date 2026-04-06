import speech_recognition as sr

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No speech detected")
            return ""

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError:
        print("Network error")
        return ""