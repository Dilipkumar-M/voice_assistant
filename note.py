from assistant import speak
import os

NOTES_FILE = "notes.txt"

def create_note():
    speak("What should I write in the note sir?")
    note = input("Note: ")
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    speak("Note added successfully sir.")

def list_notes():
    if not os.path.exists(NOTES_FILE):
        speak("No notes found sir.")
        return
    speak("Here are your notes sir:")
    with open(NOTES_FILE, "r") as f:
        for line in f:
            speak(line.strip())
