from gtts import gTTS
import os

from brain.personality import (
get_name,
get_greeting,
get_wake_word
)

def speak(text):


    text = text.replace("{name}", get_name())
    text = text.replace("{greeting}", get_greeting())
    text = text.replace("{wake}", get_wake_word())

    print("KAIRO:", text)

    tts = gTTS(text=text, lang='en')

    tts.save("assets/voice.mp3")

    os.system("start assets/voice.mp3")

