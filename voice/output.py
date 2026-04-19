#output


from gtts import gTTS
import os

def speak(text):
    print("Speaking:", text)
    tts = gTTS(text=text, lang='en')
    tts.save("assets/voice.mp3")
    os.system("start assets/voice.mp3")

#   import pyttsx3

#engine = pyttsx3.init()
#engine.setProperty('rate', 180)

#def speak(text):
#    print("KAIRO:", text)
#    engine.say(text)
#    engine.runAndWait() 