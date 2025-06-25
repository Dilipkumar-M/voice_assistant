
from assistant import greet_user, speak, get_system_info
from note import create_note, list_notes
from reminder import add_reminder, list_reminders, start_reminder_thread
from weather import get_weather
from news import get_top_headlines
from translate import translate_text
from send_email import send_email

def main():
    greet_user()
    start_reminder_thread()

    while True:
        speak("Sir,give me the command")
        command = input("Command: ").lower()

        if command == "note":
            create_note()
        elif command == "list notes":
            list_notes()
        elif command == "add reminder":
            add_reminder()
        elif command == "list reminders":
            list_reminders()
        elif command == "weather":
            get_weather()
        elif command == "sysinfo":
            get_system_info()
        elif command == "news":
            get_top_headlines()
        elif command == "translate":
            translate_text()
        elif command == "email":
            send_email()
        elif command == "exit":
            speak("It was nice to assist you sir,have a good day!")
            break
        else:
            speak("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
