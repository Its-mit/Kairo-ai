#command_router.py
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

def handle_command(command):
    print(f"User said: {command}")

    # 1. Hardcoded emergency exit commands
    if "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()
        return

    elif "change your name" in command:
        speak("Opening profile settings")
        open_setup_gui()
        speak("Profile updated successfully")
        return

    # 2. Ask Llama 3.1 to intelligently break down complex commands
    parsed_data = get_smart_intent(command)
    print(f"🧠 AI Parsed Intent: {parsed_data}")

    intent = parsed_data.get("intent")
    target = parsed_data.get("target", command)
    browser = parsed_data.get("browser", "default")
    topic = parsed_data.get("topic", "")

    # 3. Handle complex AI Intents
    if intent == "PLAY_SONG":
        if browser != "default":
            speak(f"Playing {target} on {browser}")
        else:
            speak(f"Playing {target}")
        play_song(target, browser)
        return

    elif intent == "OPEN":
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
            speak(f"Opening {target}")
            open_app(target)
        return

    elif intent == "CLOSE":
        speak(f"Closing {target}")
        speak(close_app(target))
        return

    elif intent == "MAXIMIZE":
        speak(maximize_app(target))
        return

    elif intent == "MINIMIZE":
        speak(minimize_app(target))
        return

    elif intent == "WRITE_CONTENT":
        speak(f"Working on your document about {topic}")
        ai_prompt = f"Write a complete, professional document/email about: {topic}. Output ONLY the final text that should be pasted. No introductory or concluding remarks."
        generated_content = ask_ai(ai_prompt)
        
        open_app(target)
        app_name = target.lower()
        
        if "word" in app_name or "excel" in app_name:
            time.sleep(6) 
            pyautogui.press("enter") 
            time.sleep(2)
        elif "notepad" in app_name:
            time.sleep(2)
            pyautogui.hotkey("ctrl", "n") 
            time.sleep(1)
        else:
            time.sleep(3) 
            
        pyperclip.copy(generated_content)
        pyautogui.hotkey("ctrl", "v")
        speak(f"I have finished writing the {target} document.")
        return

    # 4. Fallback for Simple Commands (Time, Date, Search, WhatsApp)
    basic_intent = detect_intent(command)
    print(f"⚙️ Basic Intent Fallback: {basic_intent}")

    if basic_intent == "NEXT_SONG":
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