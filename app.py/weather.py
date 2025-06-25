# weather.py
import requests
from assistant import speak

def get_weather():
    API_KEY = "4199de8171ce22bf917ecc5358b58f81" 
    speak("Please enter your city name.")
    city = input("City: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            message = data.get("message", "Unknown error")
            speak(f"Failed to get weather for {city}. Reason: {message}")
            return

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        report = (f"The weather in {city} is currently {weather}, "
                  f"with a temperature of {temp}°C, feels like {feels_like}°C, "
                  f"and humidity of {humidity} percent.")
        speak(report)

    except Exception as e:
        speak("There was an error retrieving the weather data.")
        print("DEBUG ERROR:", str(e))  
