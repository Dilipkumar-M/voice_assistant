# reminder.py
from assistant import speak
import threading
import time

reminders = []

def add_reminder():
    try:
        speak("Enter reminder message sir:")
        message = input("Message: ")

        speak("Sir, enter time in seconds from now:")
        delay = int(input("Time (seconds): "))

        reminder_time = time.time() + delay
        reminders.append((reminder_time, message))

        speak("Reminder set successfully.")
    except Exception as e:
        speak("Sorry sir, I couldn't set the reminder.")
        print("DEBUG: Error setting reminder:", e)

def list_reminders():
    if not reminders:
        speak("No reminders set sir.")
        return

    speak("Sir, your current reminders are:")
    now = time.time()
    for reminder_time, msg in reminders:
        seconds_left = int(reminder_time - now)
        if seconds_left > 0:
            speak(f"In {seconds_left} seconds: {msg}")
        else:
            speak(f"Due: {msg}")

def reminder_loop():
    while True:
        now = time.time()
        for r in reminders[:]:  # Create a shallow copy to iterate safely
            if now >= r[0]:
                speak(f"Reminder: {r[1]}")
                reminders.remove(r)
        time.sleep(1)

def start_reminder_thread():
    thread = threading.Thread(target=reminder_loop, daemon=True)
    thread.start()
