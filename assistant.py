import datetime
import platform
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Jimmie:",text)
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning Sir!")
    elif hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
    speak("I am Jimmie, your voice assistant. How can I help you sir?")

def get_system_info():
    info = f"System: {platform.system()}, Version: {platform.version()}, Processor: {platform.processor()}"
    speak(info)
