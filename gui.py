import tkinter as tk
from tkinter import scrolledtext

# ======== ALL IMPORTS =========
from voice.input import take_command
from voice.output import speak
from brain.parser import detect_intent
from brain.ai_brain import ask_ai
from modules.system_control import open_app
from modules.web import play_song, search_google
from modules.automation import send_whatsapp_message


def process_command(command):
    intent = detect_intent(command)

    if intent == "OPEN_APP":
        app = command.replace("open", "").strip()
        open_app(app)
        return f"Opening {app}"

    elif intent == "PLAY_SONG":
        song = command.replace("play", "").strip()
        play_song(song)
        return f"Playing {song}"

    elif intent == "SEND_WHATSAPP_SMART":
        try:
            parts = command.split("to")
            message = parts[0].replace("send", "").replace("message", "").strip()
            name = parts[1].strip()

            result = send_whatsapp_message(name, message)
            return result
        except:
            return "Error sending message"

    else:
        return ask_ai(command)


def run_ai():
    command = take_command()
    if not command:
        return

    chat.insert(tk.END, f"You: {command}\n")

    response = process_command(command)

    chat.insert(tk.END, f"Kairo: {response}\n\n")
    speak(response)

# ========= GUI =========
root = tk.Tk()
root.title("KAIRO AI")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="KAIRO AI", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="cyan")
title.pack(pady=10)

chat = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, bg="#121212", fg="white")
chat.pack(padx=10, pady=10)

btn = tk.Button(root, text="🎤 Speak", command=run_ai, bg="cyan", height=2, width=20)
btn.pack(pady=10)

root.mainloop()