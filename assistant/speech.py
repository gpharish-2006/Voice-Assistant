import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

recognizer = sr.Recognizer()


def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            print("Listening...")
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)

            return text.lower()

    except Exception:
        return ""