try:
    import speech_recognition as sr
except ImportError:
    raise ImportError("The 'speech_recognition' package is not installed. Install it with: pip install SpeechRecognition")
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import webbrowser
from fuzzywuzzy import fuzz

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice

def talk(text):
    """Speak out text and also print it."""
    print(f"SONA: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for user voice input and convert to text."""
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        talk("Sorry, I didn’t catch that. Can you repeat?")
        return ""
    except sr.RequestError:
        talk("Network issue with Google services.")
        return ""

def wish_user():
    """Greet user depending on time of day."""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        greet = "Good morning!"
    elif 12 <= hour < 18:
        greet = "Good afternoon!"
    else:
        greet = "Good evening!"
    talk(f"{greet} I’m SONA, your personal voice assistant. How can I help?")

def match_command(user_command, options):
    """Check if user command matches one of the options using fuzzy logic."""
    for option in options:
        if fuzz.partial_ratio(user_command, option) > 70:  # similarity threshold
            return True
    return False

def show_help():
    """List available commands."""
    help_text = """
I can help you with the following commands:
- Play music on YouTube (say: play despacito, play music)
- Tell the current time (say: what time is it, current time)
- Search Wikipedia (say: who is Albert Einstein, tell me about Python)
- Tell you about Abdul Kalam
- Tell a joke (say: tell me a joke, make me laugh)
- Search Google (say: search artificial intelligence)
- Open Chrome (say: open chrome, launch chrome)
- Open VS Code (say: open code, open vs code)
- Open YouTube, Google, or Gmail (say: open youtube, open google, open gmail)
- Exit the assistant (say: exit, stop, bye)
"""
    talk(help_text)

def run_sona():
    """Main logic to handle commands."""
    command = take_command()
    if command == "":
        return

    # === HELP ===
    if match_command(command, ["help", "what can you do", "commands", "options"]):
        show_help()

    # === MUSIC PLAY ===
    elif match_command(command, ["play", "play song", "play music"]):
        song = command.replace("play", "").replace("music", "").strip()
        if song:
            talk(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
        else:
            talk("Which song should I play?")

    # === TIME ===
    elif match_command(command, ["time", "what's the time", "current time", "tell me the time"]):
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time}")

    # === WIKIPEDIA SEARCH ===
    elif match_command(command, ["who is", "tell me about", "what is"]):
        person = command.replace("who is", "").replace("tell me about", "").replace("what is", "").strip()
        if person:
            try:
                info = wikipedia.summary(person, sentences=2)
                talk(info)
            except:
                talk(f"Sorry, I couldn’t find information about {person}.")
        else:
            talk("Whom should I tell you about?")

    # === CUSTOM RESPONSE (ABDUL KALAM) ===
    elif "abdul kalam" in command:
        talk("Dr. A.P.J. Abdul Kalam, the Missile Man of India, was a visionary scientist and the 11th President of India. He inspired millions with his humility, wisdom, and dreams for youth empowerment.")

    # === JOKES ===
    elif match_command(command, ["joke", "make me laugh", "tell me a joke"]):
        talk(pyjokes.get_joke())

    # === GOOGLE SEARCH ===
    elif match_command(command, ["search", "google"]):
        query = command.replace("search", "").replace("google", "").strip()
        if query:
            talk(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            talk("What do you want me to search for?")

    # === OPEN APPS ===
    elif match_command(command, ["open chrome", "launch chrome", "google chrome"]):
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome")
            os.startfile(chrome_path)
        else:
            talk("Chrome not found")

    elif match_command(command, ["open code", "open vs code", "launch vscode", "open visual studio code"]):
        talk("Opening VS Code")
        os.system("code")

    # === OPEN WEBSITES ===
    elif match_command(command, ["open youtube", "youtube"]):
        talk("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif match_command(command, ["open google", "google homepage"]):
        talk("Opening Google")
        webbrowser.open("https://google.com")

    elif match_command(command, ["open gmail", "gmail", "open email"]):
        talk("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    # === EXIT ===
    elif (
    "exit" in command 
    or "stop" in command 
    or "shutdown" in command 
    or "thanks" in command 
    or "thanks sona" in command 
    or "thank you sona" in command
    or "bye" in command
    or "see you later" in command
    ):
        talk("Okay, see you later. Take care!")
        engine.stop()   # Stop TTS engine safely
        sys.exit(0)

    else:
        talk("I heard you, but I don’t understand that yet. Say 'help' to know what I can do.")

# === RUN SONA ===
if __name__ == "__main__":
    talk("Hello, I'm SONA – your personal voice assistant,How can I help you?")
    wish_user()
    while True:
        run_sona()
