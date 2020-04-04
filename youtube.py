import webbrowser
import random
import speech_recognition as sr
import pyttsx3

complete_a = ["You got it sir", "Will do sir", "Right away sir"]

r = sr.Recognizer()  # Recognizer object

def speak(text):  # Runs when Oracle speaks
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('voice', 'english-north')
    engine.say(text)
    engine.runAndWait()


def get_video():
    with sr.Microphone() as source:
        audio = r.listen(source)
        search = r.recognize_google(audio)
        speak(random.choice(complete_a))
    url = 'https://www.youtube.com/results?search_query='
    webbrowser.open(url + search)