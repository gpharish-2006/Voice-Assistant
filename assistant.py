import datetime
from time import sleep
import pyttsx3,wikipedia,pywhatkit,webbrowser,speech_recognition as sr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os,pyautogui,subprocess,platform

intents = {
    "play_music": [
        "play song",
        "play music",
        "play on youtube",
        "play video"
    ],
    "get_time": [
        "what is the time",
        "tell time",
        "current time"
    ],
    "get_date": [
        "what is the date",
        "today date",
        "what day is today"
    ],
    "wiki_search": [
        "tell about",
    ],
    "tell_more": [
        "tell more",
        "explain more",
        "more info"
    ],
    "open_youtube": [
        "open youtube",
        "start youtube"
    ],
    "search_web": [
        "search",
        "google"
    ],
    "open_app": [
        "open chrome",
        "open brave",
        "open vs code",
        "open code"
    ],
    "exit": [
        "exit",
        "stop",
        "goodbye"
    ],
    "volume_up": [
        "volume up",
        "increase volume"
    ],
    "volume_down": [
        "volume down",
        "decrease volume"
    ],
    "volume_mute": [
        "mute volume"
    ],
}

name = "jarvis"
r=sr.Recognizer()
wikipedia.set_lang('en')

def open_app(app):
    system = platform.system()
    if system == "Windows":
        if "chrome" in app:
            os.startfile("chrome")
        if "brave" in app:
            os.startfile("brave")
        if "code" in app or "vs code" in app:
            os.startfile("code")
    elif system == "Linux":
        if "chrome" in app:
            subprocess.Popen(["chrome"])
        if "brave" in app:
            subprocess.Popen(["brave"])
        if "code" in app or "vs code" in app:
            subprocess.Popen(["code"])
    speak(f"Opening {app}")

def volume(action):
    if action == "volume_up":
        pyautogui.press("volumeup")
        print("Volume Increased")
    if action == "volume_down":
        pyautogui.press("volumedown")
        print("Volume Decreased")
    if action == "volume_mute":
        pyautogui.press("volumemute")
        print("Volume Muted")

def speak(audio):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.say(audio)
    engine.runAndWait()
    sleep(0.5)

def command():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.5)
            print("Say something!")
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            try:
                text = r.recognize_google(audio)
                return text.lower()
            except:
                return ""

    except sr.WaitTimeoutError:
        print("Listening timed out")
        return ""
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Internet error")
        return ""
    except OSError:
        print("Microphone not accessible")
        return ""

x=[]
y=[]
for i, patterns in intents.items():
    for p in patterns:
        x.append(p)
        y.append(i)

vector = CountVectorizer()
x_vec = vector.fit_transform(x)
model = MultinomialNB()
model.fit(x_vec, y)
score = model.score(x_vec, y)

def predict_intent(text):
    vec = vector.transform([text])
    prob = max(model.predict_proba(x_vec)[0])
    if prob < 0.55:
        return ""
    return model.predict(vec)[0]

last_intent = None
last_topic = None

def perform_action(intent,text):
    if intent == "play_music":
        song = text.replace("play", "")
        print("Playing " + song)
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif intent == "get_time":
        cur_time = datetime.datetime.now().strftime("%H:%M")
        print("Current time is " + cur_time)
        speak("Current time is " + cur_time)

    elif intent == "open_app":
        open_app(text)

    elif intent == "get_date":
        cur_date = datetime.date.today()
        cur_day = datetime.datetime.now().strftime("%A")
        print(f"Today is {cur_day}, {cur_date}")
        speak(f"Today is {cur_day}, {cur_date}")

    elif intent == "wiki_search":
        query = text.replace("tell about", "").replace("who is", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            global last_intent, last_topic
            last_intent = "wiki_search"
            last_topic = query
        except wikipedia.exceptions.PageError:
            print("The requested Wikipedia page could not be found.")
        except wikipedia.exceptions.DisambiguationError:
            print(f"Disambiguation error.")
        except wikipedia.exceptions.HTTPTimeoutError:
            print("Wikipedia API request timed out.")

    elif intent == "tell_more":
        if last_intent == "wiki_search" and last_topic:
            try:
                result = wikipedia.summary(last_topic, sentences=3)
                print(result)
                speak(result)
            except:
                speak("Sorry, I didn't get that. Please try again.")
        else:
            speak("There's Nothing to tell more")

    elif intent == "open_youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif intent == "volume_up" or intent == "volume_down" or intent == "volume_mute":
        volume(intent)

    elif intent == "search_web":
        query = text.replace("search", "")
        print("Searching " + query)
        speak("Searching " + query)
        pywhatkit.search(query)

    elif intent == "exit":
        print("Goodbye")
        speak("Goodbye")
        exit()

    else:
        speak("I didn't understand that")

def main():
    speak("jarvis online")

    while True:
        text = command()
        if text == "":
            continue
        if name not in text:
            continue

        text = text.replace(name, "").strip()
        pred = predict_intent(text)
        print(f"Predicted intent: {pred} {score:.3f}")
        perform_action(pred, text)
        sleep(0.3)

if __name__ == '__main__':
    main()
