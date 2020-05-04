import os
import signal
import sys

from flask import Flask, render_template, request, jsonify
from selenium import webdriver
import pyautogui as pyautogui
import multiprocessing
import pyttsx3
import requests
from flask_cors import CORS
import pytemperature

from currency import get_currency
from mail_sender import send_mail

app = Flask(__name__)
CORS(app)


# Runs when Oracle speaks
def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english+f3')
        engine.say(text)
        engine.runAndWait()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/messages")
def messages():
    return render_template("messages.html")

@app.route("/mails")
def mails():
    return render_template("mails.html")


@app.route("/weather", methods=["POST"])
def get_weather():
    response = request.get_json()

    url = "http://api.openweathermap.org/data/2.5/weather?appid=8d73691a9132521c3a1710c13d885d6d&q=%C4%B0stanbul"
    formatted_data = []
    json_data = requests.get(url).json()
    status = json_data['weather'][0]['main']  # Rain, thunderstorm etc.
    temp = int(pytemperature.k2c(json_data["main"]["temp"])) # Changing kelvin to celcius

    formatted_data = [{"Status": status, "Temp": temp}]

    return jsonify(formatted_data)


@app.route("/email_send", methods=["POST"])
def send_email():
    response = request.get_json()
    print(response)
    status = send_mail(response["subject"], response["message"], response["to"])

    if status:
        return "success"


@app.route("/get_currency", methods=["POST"])
def getCurrency():
    response = request.get_json()
    print(response)

    data = get_currency()
    print(data)
    return jsonify(data)


@app.route("/quit", methods=["POST"])
def shut_down():
    print("got here")
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({"success": True, "message": "Server is shutting down..."})


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


def start():
    app.run(debug=True)


def opens():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("dom.webnotifications.enabled", False)
    profile.set_preference("general.useragent.override", "Mozilla/5.0")
    profile.update_preferences()
    browser = webdriver.Firefox(firefox_profile=profile, executable_path='/usr/local/bin/geckodriver')
    browser.get("http://127.0.0.1:5000/")
    pyautogui.press('f11')

    speak("Welcome to my user interface sir.")


def start_interface():
    p1 = multiprocessing.Process(target=start)
    p1.start()
    p2 = multiprocessing.Process(target=opens)
    #p2.start()

start_interface()
