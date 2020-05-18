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
import webbrowser

from todo import add_todo_item, get_todo
from currency import get_currency
from mail_sender import send_mail
from py_functions.record_command import insert_command
from car_price_knn import predict
from py_functions.sleep_recommendations import insert_bedtime, update_bedtime
from py_functions.calculate_cal import result, check_cal
from py_functions.meals_data import add_meal, get_meals

app = Flask(__name__)
CORS(app)


# Runs when Oracle speaks
def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english+f3')
        engine.say(text)
        engine.runAndWait()


# Links

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/messages")
def messages():
    return render_template("messages.html")


@app.route("/mails")
def mails():
    return render_template("mails.html")


@app.route("/todo")
def todo():
    return render_template("todo.html")

# Classic data requests

@app.route("/weather", methods=["POST"])
def get_weather():
    response = request.get_json()

    url = "http://api.openweathermap.org/data/2.5/weather?appid=8d73691a9132521c3a1710c13d885d6d&q=%C4%B0stanbul"
    formatted_data = []
    json_data = requests.get(url).json()
    status = json_data['weather'][0]['main']  # Rain, thunderstorm etc.
    temp = int(pytemperature.k2c(json_data["main"]["temp"])) # Changing kelvin to celcius

    formatted_data = [{"Status": status, "Temp": temp}]
    print(formatted_data)
    return jsonify(formatted_data)

@app.route("/get_currency", methods=["POST"])
def getCurrency():
    response = request.get_json()
    print(response)

    data = get_currency()
    print(data)
    return jsonify(data)

# Email requests


@app.route("/email_send", methods=["POST"])
def send_email():
    response = request.get_json()
    print(response)
    status = send_mail(response["subject"], response["message"], response["to"])
    print(status)
    if not status:
        return jsonify({"success": False})

    return jsonify({"success": True})

# To do page requests


@app.route("/add_todo", methods=["POST"])
def add_todo():
    response = request.get_json()
    status = add_todo_item(response["date"], response["todo"])

    if status:
        data = get_todo()
        return jsonify(data)


@app.route("/get_todo", methods=["GET"])
def getTodo():
    data = get_todo()
    return jsonify(data)


@app.route("/quit", methods=["POST"])
def shut_down():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({"success": True, "message": "Server is shutting down..."})


@app.route("/record_command", methods=["POST"])
def rec_command():
    response = request.get_json()
    print(response)

    insert_command(response["text"], response["command"], response["type"])

    return "Success"

# Price prediction systems requests


@app.route("/car_predict", methods=["POST"])
def car_predict():
    response = request.get_json()
    print(response)

    predicted_data, error_line = predict(response["brand"], response["year"], response["mileage"], response["transmission"])

    if not predicted_data:
        return jsonify({"success": False, "error_line": error_line})

    return jsonify({"success": True, "price": predicted_data[0]})


# Sleep recommendation system requests

@app.route("/record_bedtime", methods=["POST"])
def record_sleep():
    inputs = request.get_json()
    print(input)

    status = insert_bedtime(inputs["bedtime"], inputs["waketime"], inputs["date"], inputs["rate"])

    if status:
        return jsonify({"success": True})


@app.route("/update_waketime", methods=["POST"])
def update_sleep():
    input = request.get_json()
    print(input)

    status, sleep = update_bedtime(input["waketime"])

    if status:
        return jsonify({"success": True, "sleep": sleep})


# Diet requests

@app.route("/calculate_cal", methods=["POST"])
def calculate_kcal():
    input = request.get_json()
    print(input)

    kcal = result(input["gender"], input["height"], input["weight"], input["age"], input["activity"], input["aim"])

    print(kcal)
    if kcal:
        return jsonify({"success": True, "kcal": kcal})


@app.route("/check_cal", methods=["POST"])
def check_calories():
    kcal = check_cal()

    if not kcal:
        return jsonify({"kcal": ""})

    return jsonify({"kcal": kcal})


@app.route("/add_meal", methods=["POST"])
def addMeal():
    input = request.get_json()
    print(input)

    status = add_meal(input["meal"], input["type"])

    if status:
        data = get_meals()
        return jsonify(data)
    else:
        return False


@app.route("/get_meals", methods=["GET"])
def getMeals():
    print("got here")
    data = get_meals()

    return jsonify(data)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


def start():
    app.run(debug=True, use_reloader=False)


def opens():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("dom.webnotifications.enabled", False)
    profile.set_preference("general.useragent.override", "Mozilla/5.0")
    profile.update_preferences()
    browser = webdriver.Firefox(firefox_profile=profile, executable_path='/usr/local/bin/geckodriver')
    browser.get("http://127.0.0.1:5000/")
    pyautogui.press('f11')

    speak("Welcome to my user interface sir.")


def open_gui():
    url = "http://127.0.0.1:5000/"
    webbrowser.get(using='google-chrome').open(url, new=2)


def start_interface():
    p1 = multiprocessing.Process(target=start)
    p1.start()
    p2 = multiprocessing.Process(target=open_gui)
    #p2.start()


start_interface()
