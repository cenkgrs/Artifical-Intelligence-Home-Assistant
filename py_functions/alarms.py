from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import config
import sqlite3
import datetime
import pygame
import playsound
import os

stop_words = set(stopwords.words('english'))


def alarm(text):
    is_digit = False
    text = text["text"]
    clock = [int(s) for s in text.split() if s.isdigit()]

    text_tokens = word_tokenize(text)

    # Filtering text so there will be less loop
    filtered_sentence = [w for w in text_tokens if not w in stop_words]

    # Setting alarm
    if "set" or "Set" in filtered_sentence:

        if not clock:
            for index, item in enumerate(filtered_sentence):
                print(item)
                # Get the quantity and meal after it and add it to meals
                if item in config.numbers:
                    number = config.numbers.index(item)
                    clock.append(number)

            if not clock:
                return False, "You didn't give any clock info sir"

        if len(clock) == 1:
            clock.append(00)

        with sqlite3.connect("Oracle") as con:
            cursor = con.cursor()
            try:
                cursor.execute("INSERT INTO Alarms (hour, minute)"
                               "VALUES (?, ?) ", (clock[0], clock[1]))

                return True, ""
            except sqlite3.OperationalError:
                return False, "Couldn't set the alarm sir"

    else:
        return False, "Did not get that sir"


def check_alarm():
    check_hour = datetime.datetime.now().hour
    check_min = datetime.datetime.now().minute
    print(check_hour)
    print(check_min)
    with sqlite3.connect("Oracle") as con:
        try:
            db = con.execute('SELECT * FROM Alarms ORDER BY hour ASC')
            last = db.fetchmany()
            print(last)

            if check_hour == last[0][1] and check_min == last[0][2]:

                con.execute("DELETE FROM Alarms WHERE hour = ? and minute = ?", (check_hour, check_min))
                con.commit()

                return True
            else:
                return False

        except Exception as e:
            return False


