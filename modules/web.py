import pywhatkit
import wikipedia

def play_song(song):
    pywhatkit.playonyt(song)

def search_google(query):
    pywhatkit.search(query)

def get_info(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return "Sorry, I couldn't find information."