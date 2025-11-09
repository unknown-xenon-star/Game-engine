import speech_recognition as sr
import webbrowser
import pyttsx3

recogniser = sr.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50) 


def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak("Hello sir, ")
speak("Initializing Jarvis")