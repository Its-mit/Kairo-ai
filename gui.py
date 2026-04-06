import tkinter as tk
from voice.input import take_command
from voice.output import speak
from brain.parser import detect_intent
from modules.system_control import open_app
from modules.web import play_song, search_google, get_info
from modules.automation import tell_time, tell_date
import datetime

def run_ai():
    command = take_command()

    if not command:
        return

    user_text.set("You: " + command)

    intent = detect_intent(command)

    if intent == "GREETING":
        response = "Hello, how can I help you?"

    elif intent == "GET_TIME":
        response = "Time is " + tell_time()

    elif intent == "GET_DATE":
        response = "Today is " + tell_date()

    elif intent == "OPEN_APP":
        app_name = command.replace("open", "").strip()
        open_app(app_name)
        response = f"Opening {app_name}"

    elif intent == "PLAY_SONG":
        song = command.replace("play", "").strip()
        play_song(song)
        response = f"Playing {song}"

    elif intent == "SEARCH_GOOGLE":
        query = command.replace("search", "").strip()
        search_google(query)
        response = f"Searching {query}"

    elif intent == "GET_INFO":
        response = get_info(command)

    else:
        response = "Sorry, I did not understand"

    ai_text.set("Kairo: " + response)
    speak(response)

# GUI Window
root = tk.Tk()
root.title("KAIRO AI Assistant")
root.geometry("500x400")

# Text Variables
user_text = tk.StringVar()
ai_text = tk.StringVar()

root.configure(bg="#1e1e1e")

tk.Label(root, text="KAIRO AI", font=("Arial", 22, "bold"), bg="#1e1e1e", fg="cyan").pack(pady=10)

tk.Label(root, textvariable=user_text, wraplength=400, bg="#1e1e1e", fg="white").pack(pady=10)
tk.Label(root, textvariable=ai_text, wraplength=400, bg="#1e1e1e", fg="lightgreen").pack(pady=10)

tk.Button(root, text="🎤 Speak", command=run_ai, height=2, width=20, bg="cyan").pack(pady=20)
# Run app
root.mainloop()