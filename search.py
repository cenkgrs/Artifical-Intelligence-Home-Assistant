from bs4 import BeautifulSoup
import requests
import pyttsx3
import lxml
import random
import speech_recognition as sr
import webbrowser
import os
import re

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
    global r
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
    global r
    audio = listen()
    query = r.recognize_google(audio)

    links = []
    to_remove = []
    clean_links = []

    url = "https://www.google.com.tr/search?q={}".format(query)
    url = "https://www.google.com/search?ei=el-HXvqxIoukgweZ3KCQAw&q=batman"
    speak(random.choice(complete_a))
    webbrowser.open(url)

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')

    results = soup.find_all("div", attrs={"ZINbbc"})
    for r in results:
        try:
            link = r.find('a', href=True)

            if link != '':
                links.append(link['href'])

        except:
            continue

    for i, l in enumerate(links):
        clean = re.search('\/url\?q\=(.*)\&sa', l)

        # Anything that doesn't fit the above pattern will be removed
        if clean is None:
            to_remove.append(i)
            continue
        clean_links.append(clean.group(1))

    speak("Which link you want to open boss ?")

    audio = listen()
    choice = r.recognize_google(audio)

    webbrowser.open(links[int(choice) - 1])

search()