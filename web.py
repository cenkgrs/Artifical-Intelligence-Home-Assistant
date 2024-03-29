import os
import signal

from flask import Flask, render_template, request, jsonify, Response
from selenium import webdriver
import pyautogui as pyautogui
import multiprocessing
import pyttsx3
import requests
from flask_cors import CORS
import pytemperature
import webbrowser
from datetime import datetime, timedelta
import cv2
import time

from real_time_detection import *
from todo import add_todo_item, get_todo
from currency import get_currency
from mail_sender import send_mail
from py_functions.gmail import get_mails
from py_functions.record_command import insert_command, get_command_to_txt
from car_price_knn import predict
from py_functions.sleep_recommendations import insert_bedtime, update_bedtime
from py_functions.calculate_cal import result, check_cal
from py_functions.meals_data import *
from py_functions.alarms import alarm, check_alarm, get_alarms
from py_functions.weather_informations import get_weather_request
from book_recommendation import get_book_matches, get_book_recommendations
from weather_prediction import get_predictions
from face_rec_webcam import show_webcam
from py_functions.calendar import add_calendar_info, get_calendar_info

app = Flask(__name__)
CORS(app)

# Real time streaming object
# VIDEO = VideoStreaming()


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
    temp = int(pytemperature.k2c(json_data["main"]["temp"]))  # Changing kelvin to celcius
    temp_min = int(pytemperature.k2c(json_data["main"]["temp_min"]))
    temp_max = int(pytemperature.k2c(json_data["main"]["temp_max"]))
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]

    wind = json_data["wind"]["speed"]

    sunrise = json_data["sys"]["sunrise"]
    sunrise = datetime.datetime.utcfromtimestamp(sunrise) + timedelta(hours=3)  # Converting unix time to timestamp
    sunrise = sunrise.strftime('%H:%M:%S')

    sunset = json_data["sys"]["sunset"]
    sunset = datetime.datetime.utcfromtimestamp(sunset) + timedelta(hours=3)  # Converting unix time to timestamp
    sunset = sunset.strftime('%H:%M:%S')

    formatted_data = [{"Status": status, "Temp": temp, "temp_min": temp_min, "temp_max": temp_max,
                       "pressure": pressure, "humidity": humidity, "wind": wind, "temp_max": temp_max,
                       "sunrise": sunrise, "sunset": sunset}]

    return jsonify(formatted_data)


@app.route("/get_currency", methods=["POST"])
def getCurrency():
    response = request.get_json()

    data = get_currency()
    print(data)
    return jsonify(data)

# Email requests


@app.route("/email_send", methods=["POST"])
def send_email():
    response = request.get_json()
    status = send_mail(response["subject"], response["message"], response["to"])

    if not status:
        return jsonify({"success": False})

    return jsonify({"success": True})


@app.route("/get_emails", methods=["GET"])
def getEmails():
    data = get_mails()

    return jsonify(data)


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

    predicted_data, error_line = predict(response["brand"], response["year"], response["mileage"],
                                         response["transmission"])

    if not predicted_data:
        return jsonify({"success": False, "error_line": error_line})

    return jsonify({"success": True, "price": predicted_data[0]})


# Book Recommendation System
@app.route("/get_book_input", methods=["POST"])
def getBookInput():
    input = request.get_json()

    data = get_book_matches(input["inp"])

    if data:
        return jsonify(data)
    else:
        return jsonify({"status": False})


@app.route("/get_book_recommendation", methods=["POST"])
def getBookRecommendation():
    input = request.get_json()

    data = get_book_recommendations(input["book_name"])
    if data:
        return jsonify(data)
    else:
        return jsonify({"status": False})


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

# Weather predict system requests


@app.route("/get_weather_prediction", methods=["POST"])
def getWeatherPrediction():
    input = request.get_json()

    weather_predictions = get_predictions(input["weather_data"])
    print(weather_predictions)

    if weather_predictions:
        return jsonify({"data": weather_predictions})


@app.route("/get_weather_information", methods=["POST"])
def getWeatherInformation():
    input = request.get_json()

    day, weather_information = get_weather_request(input["text"])
    print(weather_information)

    if weather_information:
        return jsonify({"data": weather_information, "day": day})


# Diet requests

@app.route("/calculate_cal", methods=["POST"])
def calculate_kcal():
    input = request.get_json()

    data = result(input["gender"], input["height"], input["weight"], input["age"], input["activity"], input["aim"])

    if data:
        return jsonify({"success": True, "data": data})
    else:
        return jsonify({"success": False})


@app.route("/check_cal", methods=["POST"])
def check_calories():
    data = check_cal()

    if not data:
        return jsonify({"success": False})

    return jsonify({"success": True, "data": data})


@app.route("/add_meal", methods=["POST"])
def addMeal():
    input = request.get_json()

    status = add_meal(input["meal"], input["type"], input["meal-id"], input["meal-gram"])

    if status:
        data = get_meals()
        return jsonify(data)
    else:
        return jsonify({"status": False})


@app.route("/get_meals", methods=["GET"])
def getMeals():
    data = get_meals()
    print(data)
    return jsonify(data)


@app.route("/get_meal_input", methods=["POST"])
def getMealInput():
    input = request.get_json()

    data = get_meal_input(input["inp"])

    if data:
        return jsonify(data)
    else:
        return jsonify({"status": False})


@app.route("/add_meal_natural", methods=["POST"])
def addMealNatural():
    text = request.get_json()

    status, error = add_meal_natural(text)
    print(status, error)
    if status:
        data = get_meals()
        return jsonify(data)
    else:
        return jsonify({"status": status, "error": error})


@app.route("/get_meal_recommendation", methods=["GET"])
def getMealRecommendation():

    # If True there is data if False there is a error statement
    data, status = get_meal_recommendation()
    print(data, status)

    return jsonify({"data": data, "status": status})


# Alarm requests
@app.route("/alarm", methods=["POST"])
def prepare_alarm():
    text = request.get_json()

    status, error = alarm(text)

    if status and error == "":
        return jsonify(status)
    elif status and error != "":
        return jsonify({"status": status, "action": error})
    else:
        return jsonify({"status": status, "error": error})


@app.route("/check_alarm", methods=["GET"])
def checkAlarm():
    status = check_alarm()
    if status:
        return jsonify({"status": "alarm"})

    return jsonify({"status": "no alarm"})


@app.route("/get_alarms", methods=["GET"])
def getAlarms():
    data = get_alarms()

    if data:
        return jsonify({"data": data})

    return jsonify({"data": ""})


# Film requests

@app.route("/get_film_list", methods=["GET"])
def getFirmList():
    path = "static/posters/"
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    return jsonify(onlyfiles)


# Calendar requests

@app.route("/add_calendar_info", methods=["POST"])
def addCalendarInfo():
    inputs = request.get_json()

    status, error = add_calendar_info(inputs)

    if error == "":
        data, error = get_calendar_info()
        return jsonify({"response": data, "error": error})

    return jsonify({"status": status, "error": error})


@app.route("/get_calendar_info", methods=["GET"])
def getCalendarInfo():

    data, error = get_calendar_info()

    return jsonify({"response": data, "error": error})

# Music requests
@app.route("/get_music_list", methods=["GET"])
def getMusicList():

    path = "static/audio/"
    from os import listdir
    from os.path import isfile, join
    musics = [f for f in listdir(path) if isfile(join(path, f))]
    print(musics)

    return jsonify(musics)


# Live stream request

@app.route('/video_feed')
def video_feed():
    '''
    Video streaming route.
    '''
    return Response(
        # Runs show webcam function
        show_webcam(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


def start():
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)


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
    # p2.start()


start_interface()