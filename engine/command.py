import pyttsx3
import speech_recognition as sr
import eel
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pkg_resources')



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
        eel.Displaymessage("Listening...")

        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            eel.Displaymessage("Mic timeout, please speak louder.")
            print("Microphone timeout.")
            return ""

        try:
            print("Recognizing...")
            eel.Displaymessage("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            eel.Displaymessage(query)
            speak(query)
            eel.Showhood()
            return query.lower()

        except Exception as e:
            eel.Displaymessage("Could not recognize speech.")
            print("Recognition error:", e)
            return ""

