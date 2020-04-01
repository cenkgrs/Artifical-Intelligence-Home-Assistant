from oracle import speak
import webbrowser
import random
import speech_recognition as sr

complete_a = ["You got it sir", "Will do sir", "Right away sir"]

r = sr.Recognizer() # Recognizer object

def get_video():
    with sr.Microphone() as source:
        audio = r.listen(source)
        search = r.recognize_google(audio)
        speak(random.choice(complete_a))
    url = 'https://www.youtube.com/results?search_query='
    webbrowser.open(url + search)