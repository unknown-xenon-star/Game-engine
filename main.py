import speech_recognition as sr
import webbrowser
import pyttsx3

recogniser = sr.Recognizer()
##ttsx = pyttsx3.init()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak("hello sir")
speak("Initializing Jarvis")
