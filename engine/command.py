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

@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except Exception as e:
            print("Microphone Listening Error:", e)
            return ""

        try:
            print("Recognizing...")
            eel.DisplayMessage("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            eel.DisplayMessage(query)
            speak(query)
            eel.ShowHood()
        except Exception as e:
            return ""

        return query.lower()
