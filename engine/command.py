import pyttsx3
import speech_recognition as sr
import eel


def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 150)
    print(voices)
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print("recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")

    except Exception as e:
        return ""

    return query.lower()


text = takecommand()

if text:
    speak(text)
else:
    speak("I didn't catch that. Please try again.")
