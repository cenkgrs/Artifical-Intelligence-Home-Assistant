from bs4 import BeautifulSoup
import requests
import pyttsx3
import lxml
import random
import speech_recognition as sr
import webbrowser
import os
r = sr.Recognizer()

complete_a = ["You got it sir", "Will do sir", "Right away sir"]


# Runs when Oracle speaks
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('voice', 'english+f3')
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        try:
            os.system('play -nq -t alsa synth {} sine {}'.format(0.15,
                                                                 500))  # 1 = duration, 440 = frequency -> this sounds a beep
            audio = r.listen(source)
            return audio
        except sr.UnknownValueError:
            speak("Did not get that sir")
            print("Google Speech Recognition could not understand audio")
            listen()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def search():
    audio = listen()
    query = r.recognize_google(audio)

    url = "https://www.google.com.tr/search?q={}".format(query)
    speak(random.choice(complete_a))
    webbrowser.open(url)

    speak("Which link you want to open boss ?")