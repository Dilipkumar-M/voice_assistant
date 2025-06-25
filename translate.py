from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import tempfile
import time
from assistant import speak

def speak_translated(text, lang):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_path = fp.name
            tts.save(temp_path)
        
        pygame.mixer.init()
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)
    except Exception as e:
        speak("Sorry Sir, I couldn't speak the translated text.")
        print("gTTS Error:", e)

def translate_text():
    speak("Sir, please enter the text you want to translate.")
    text = input("Text: ")

    speak("Enter the destination language code sir.")
    dest_lang = input("Language code: ").strip()

    try:
        translated = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        result = f"Sir, the translation in {dest_lang} is: {translated}"
        speak(result)  # Speaks the message in English
        speak_translated(translated, dest_lang)  # Speaks in translated language
    except Exception as e:
        speak("Sorry Sir, I couldn't translate the text.")
        print("Sir, it's an Error:", e)
