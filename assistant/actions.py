import datetime
import wikipedia
import webbrowser
import pywhatkit

from assistant.speech import speak

last_topic = None


def perform_action(intent, text):

    global last_topic

    if intent == "play_music":

        song = text.replace("play", "")

        speak(f"Playing {song}")

        pywhatkit.playonyt(song)

    elif intent == "get_time":

        current_time = datetime.datetime.now().strftime("%H:%M")

        speak(f"Current time is {current_time}")

    elif intent == "get_date":

        today = datetime.date.today()

        speak(f"Today's date is {today}")

    elif intent == "wiki_search":

        query = (
            text.replace("tell about", "")
            .replace("who is", "")
        )

        try:

            result = wikipedia.summary(query, sentences=2)

            last_topic = query

            speak(result)

            return result

        except:
            return "Wikipedia result not found"

    elif intent == "open_youtube":

        webbrowser.open("https://youtube.com")

        speak("Opening YouTube")

    elif intent == "search_web":

        query = text.replace("search", "")

        pywhatkit.search(query)

        speak(f"Searching {query}")

    elif intent == "exit":

        speak("Goodbye")

        exit()

    else:

        speak("I did not understand")

        return "Unknown command"