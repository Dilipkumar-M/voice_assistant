import requests
from assistant import speak

API_KEY = "f6a08d240aa85063a7c6eae1a61c6ce6"

def get_top_headlines():
    speak("Fetching the top news headlines.")
    url = f"http://api.mediastack.com/v1/news?access_key={API_KEY}&countries=in&limit=5"

    try:
        response = requests.get(url)
        data = response.json()

        articles = data.get("data", [])

        if not articles:
            speak("Sir, no news articles were found.")
            return

        for idx, article in enumerate(articles, 1):
            title = article.get("title", "No title")
            if title:
                speak(f"News {idx}: {title}")

    except Exception as e:
        speak("Sir, there was an error while fetching the news.")
        print("DEBUG ERROR:", e)
