import pywhatkit
import wikipedia
import webbrowser
import urllib.request
import urllib.parse
import re

def play_song(song, browser="default"):
    try:
        # 1. Search YouTube and scrape the first video ID invisibly
        query_string = urllib.parse.urlencode({"search_query": song})
        html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        
        if not search_results:
            return "Could not find the song."

        # Reconstruct the direct video link
        video_url = "https://www.youtube.com/watch?v=" + search_results[0]
        
        # 2. Open the video in the requested browser
        if browser == "brave":
            # NOTE: Check if this path matches where Brave is installed on your PC
            brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
            webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
            webbrowser.get('brave').open(video_url)
            
        elif browser == "chrome":
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(video_url)
            
        else:
            # Fallback to the system's default browser
            webbrowser.open(video_url)
            
    except Exception as e:
        print("ERROR:", e)
        return "Error trying to play the song."

def search_google(query):
    pywhatkit.search(query)

def get_info(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return "Sorry, I couldn't find information."