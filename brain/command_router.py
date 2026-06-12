import time
import pyperclip
import pyautogui
from brain.parser import detect_intent
from brain.ai_brain import get_smart_intent, ask_ai
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
    print(f"User said: {command}")

    # 1. Hardcoded emergency exit commands
    if "exit" in command or "stop" in command:
        speak("Goodbye")
        exit() # Exits the program entirely
        return

    elif "change your name" in command:
        speak("Opening profile settings")
        open_setup_gui()
        speak("Profile updated successfully")
        return

    # 2. Ask Llama 3.1 to intelligently break down complex commands
    parsed_data = get_smart_intent(command)
    print(f"🧠 AI Parsed Intent: {parsed_data}")

    # Define all variables clearly so Pylance doesn't throw errors
    intent = parsed_data.get("intent")
    target = parsed_data.get("target", command)
    browser = parsed_data.get("browser", "default")
    topic = parsed_data.get("topic", "")

    # 3. Handle complex AI Intents (Writing, Open apps/websites, and playing songs)
    if intent == "WRITE_CONTENT":
        speak(f"Sure, creating a draft about {topic} in {target}.")
        
        # Step A: Open the targeted application
        open_app(target)
        
        # Step A.1: Force the app to open a BLANK canvas
        if "word" in target or "excel" in target or "powerpoint" in target:
            time.sleep(6) # Office apps are heavy, wait for Home Screen
            pyautogui.press('enter') # Hits 'Blank Document'
            time.sleep(2) # Wait for the blank canvas to load
            
        elif "mail" in target or "email" in target:
            time.sleep(3) # Wait for mail to load
            pyautogui.hotkey('ctrl', 'n') # Shortcut for New Email
            time.sleep(1)
            
        elif "notepad" in target:
            time.sleep(2) # Wait for notepad
            pyautogui.hotkey('ctrl', 'n') # Shortcut for New Tab/Window
            time.sleep(1)
            
        else:
            time.sleep(3) # Generic wait for any other app
            
        # Step B: Generate the detailed content via Llama 3.1
        speak("Thinking about what to write...")
        generation_prompt = f"Write a professional and complete document/text about: {topic}. Do not include conversational remarks, just write the content directly."
        generated_text = ask_ai(generation_prompt)
        
        # Step C: Copy generated text to clipboard and paste it instantly
        pyperclip.copy(generated_text)
        pyautogui.hotkey('ctrl', 'v')
        
        speak(f"I have successfully written the content in {target}.")
        return

    elif intent == "PLAY_SONG":
        if browser != "default":
            speak(f"Playing {target} on {browser}")
        else:
            speak(f"Playing {target}")
            
        play_song(target, browser)
        return

    elif intent == "OPEN":
        # Check if the AI determined it's a website rather than a desktop app
        if browser != "default" or target.lower() in ["youtube", "google", "facebook", "instagram"]:
            speak(f"Opening {target} in the browser")
            
            import webbrowser
            url = f"https://www.{target.lower().replace(' ', '')}.com"
            
            if browser == "brave":
                brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
                webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
                webbrowser.get('brave').open(url)
            elif browser == "chrome":
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open(url)
            else:
                webbrowser.open(url)
        else:
            # It's a normal desktop app
            speak(f"Opening {target}")
            open_app(target)
        return

    # 4. If the AI didn't catch a complex action, fall back to basic old-school keywords
    basic_intent = detect_intent(command)
    print(f"⚙️ Basic Intent Fallback: {basic_intent}")

    if basic_intent == "CLOSE_APP":
        app = extract_app_name(command, "close")
        speak(close_app(app))

    elif basic_intent == "MAXIMIZE_APP":
        app = extract_app_name(command, "maximize")
        speak(maximize_app(app))

    elif basic_intent == "MINIMIZE_APP":
        app = extract_app_name(command, ["minimize", "minimise", "minimixe"])
        speak(minimize_app(app))

    elif basic_intent == "NEXT_SONG":
        speak(next_song())

    elif basic_intent == "PREVIOUS_SONG":
        speak(previous_song())

    elif basic_intent == "PAUSE_SONG":
        speak(play_pause())

    elif basic_intent == "SEARCH_GOOGLE":
        query = command.replace("search", "").strip()
        speak(f"Searching {query}")
        search_google(query)

    elif basic_intent == "GET_INFO":
        speak("Searching for information")
        speak(get_info(command))

    elif basic_intent == "GET_TIME":
        speak(f"The time is {tell_time()}")

    elif basic_intent == "GET_DATE":
        speak(f"Today is {tell_date()}")

    elif basic_intent == "SEND_WHATSAPP_SMART":
        try:
            parts = command.split("to")
            message = parts[0].replace("send", "").replace("message", "").strip()
            name = parts[1].strip()
            speak(f"Sending message to {name}")
            speak(send_whatsapp_message(name, message))
        except Exception as e:
            print("ERROR:", e)
            speak("Sorry, I couldn't understand the WhatsApp command")

    # 5. Total fallback: General conversational AI
    else:
        response = ask_ai(command)
        speak(response)