from weather_prediction import get_predictions
import requests
import pytemperature
from datetime import datetime, timedelta

date = datetime.now()
day = str(date.day)
month = date.month if date.month > 9 else "0" + str(date.month)

today = day + "." + month  # 28.05


def get_weather_request(text):
    print(text)

    text_backup = text.split(" ")

    # Get meal time from text_backup
    for i in text_backup:
        if i == "today" or i == "tomorrow" or i == "week":
            day_info = i

    # If command like " get weather info " return today's weather info
    if day_info == "":
        day_info = "today"

    if day_info == "today":
        return "today", get_weather_today()
    elif day_info == "tomorrow":
        return "tomorrow", get_weather_tomorrow()


def get_weather_today():
    formatted_data = []

    url = "http://api.openweathermap.org/data/2.5/weather?appid=8d73691a9132521c3a1710c13d885d6d&q=%C4%B0stanbul"
    json_data = requests.get(url).json()

    status = json_data['weather'][0]['main']  # Rain, thunderstorm etc.
    temp = int(pytemperature.k2c(json_data["main"]["temp"]))  # Changing kelvin to celcius

    temp_min = int(pytemperature.k2c(json_data["main"]["temp_min"]))
    temp_max = int(pytemperature.k2c(json_data["main"]["temp_max"]))

    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]

    wind = json_data["wind"]["speed"]

    sunrise = json_data["sys"]["sunrise"]
    sunrise = datetime.utcfromtimestamp(sunrise) + timedelta(hours=3)  # Converting unix time to timestamp
    sunrise = sunrise.strftime('%H:%M:%S')

    sunrise = sunrise.split(":")
    sunrise = float(str(int(sunrise[0])) + '.' + str(int(sunrise[1])))

    sunset = json_data["sys"]["sunset"]
    sunset = datetime.utcfromtimestamp(sunset) + timedelta(hours=3)  # Converting unix time to timestamp
    sunset = sunset.strftime('%H:%M:%S')

    sunset = sunset.split(":")
    sunset = float(str(int(sunset[0])) + '.' + str(int(sunset[1])))

    formatted_data = [{"Status": status, "Temp": temp, "temp_min": temp_min, "temp_max": temp_max,
                       "pressure": pressure, "humidity": humidity, "wind": wind, "temp_max": temp_max,
                       "sunrise": sunrise, "sunset": sunset, "date": today}]

    return formatted_data


def get_weather_tomorrow():

    data = get_weather_today()
    print(data)
    return get_predictions(data[0])
