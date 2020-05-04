from bs4 import BeautifulSoup
import requests
import pyttsx3
import lxml
import random

# Runs when Oracle speaks
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('voice', 'english+f3')
    engine.say(text)
    engine.runAndWait()


def get_currency():

    url = "https://tlkur.com/"
    response = requests.get(url)

    data = response.text
    soup = BeautifulSoup(data, 'lxml')

    usd = soup.find("span", {"id": "USDTL_rate"})
    eur = soup.find("span", {"id": "EURTL_rate"})
    pound = soup.find("span", {"id": "GBPTL_rate"})

    data = [{
        "usd":      round(float(usd.text), 1),
        "eur":      round(float(eur.text), 1),
        "pound":    round(float(pound.text), 1),
        "status":   True
    }]

    return data


'''
    speak(f"US Dollar is {round(float(usd.text), 1)}")
    speak(f"and EURO is {round(float(eur.text), 1)} ")
    speak(f"and Pound is {round(float(pound.text), 1)}")
'''