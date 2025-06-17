import pyttsx3
import speech_recognition as sr
import eel


import pyttsx3
import speech_recognition as sr
import eel


def speak(text):
    try:
        engine = pyttsx3.init("sapi5")

        # List all available voices
        voices = engine.getProperty("voices")
        print("Available Voices:")
        for idx, voice in enumerate(voices):
            print(f"{idx}: {voice.name} - {voice.id}")

        # You can change the index here if needed
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 174)

        print("Speaking:", text)
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("TTS Error:", e)
        print("Try checking your audio output settings or use an alternative TTS library.")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except Exception as e:
            print("Microphone Listening Error:", e)
            return ""

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()

        except Exception as e:
            return ""


text = takecommand()
speak(text)



"""def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 174)
    print(voices)
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
            eel.display(query)  # Call the eel function to display the text
        except Exception as e:
            return ""

        return query.lower()


text = takecommand()
speak(text)"""
