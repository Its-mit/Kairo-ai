from gtts import gTTS
import os
import pygame
import time

from brain.personality import (
    get_name,
    get_greeting,
    get_wake_word
)

# Initialize the pygame audio mixer once
pygame.mixer.init()

def speak(text):
    text = text.replace("{name}", get_name())
    text = text.replace("{greeting}", get_greeting())
    text = text.replace("{wake}", get_wake_word())

    print("KAIRO:", text)

    # Ensure the directory exists
    os.makedirs("assets", exist_ok=True)
    audio_file = "assets/voice.mp3"

    tts = gTTS(text=text, lang='en')
    tts.save(audio_file)

    # Load and play the audio seamlessly
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Keep the program waiting while Kairo is actively speaking
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
        
    # Unload the file so it can be overwritten next time Kairo speaks
    try:
        pygame.mixer.music.unload()
    except AttributeError:
        pass # Handle older versions of pygame