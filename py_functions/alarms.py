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

    # Get array of numbers from text
    clock = [int(s) for s in text.split() if s.isdigit()]
    print(clock)
    text_tokens = word_tokenize(text)

    # Filtering text so there will be less loop - if token not a stop word add to filtered_sentence array
    filtered_sentence = [w for w in text_tokens if not w in stop_words]
    print(filtered_sentence)
    # Setting alarm
    if "set" in filtered_sentence or "Set" in filtered_sentence:

        # If there isn't any number in text (like 5 10 not five ten)
        if not clock:
            for index, item in enumerate(filtered_sentence):
                print(item)
                # Get the quantity and meal after it and add it to meals
                if item in config.numbers:
                    number = config.numbers.index(item)
                    clock.append(number)

            if not clock:
                return False, "You didn't give any clock info sir"

        if len(clock) == 1 and len(str(clock[0])) < 3:
            clock.append(00)
        elif len(str(clock[0])) > 2:
            # If number is like 2130(error at speech rec) convert it to 21 30
            min, clock[0] = int(str(clock[0])[2] + str(clock[0])[3]), int(str(clock[0])[0] + str(clock[0])[1])
            clock.append(min)

        with sqlite3.connect("Oracle") as con:
            cursor = con.cursor()
            try:
                cursor.execute("INSERT INTO Alarms (hour, minute)"
                               "VALUES (?, ?) ", (clock[0], clock[1]))

                return True, ""
            except sqlite3.OperationalError:
                return False, "Couldn't set the alarm sir"

    elif "show" in filtered_sentence or "open" in filtered_sentence:
        return True, "show"
    elif "delete" in filtered_sentence or "turn off" in filtered_sentence:
        delete_alarms()

        return True, "delete"
    else:
        return False, "Did not get that sir"


def check_alarm():
    check_hour = datetime.datetime.now().hour
    check_min = datetime.datetime.now().minute

    with sqlite3.connect("Oracle") as con:
        try:
            db = con.execute('SELECT * FROM Alarms ORDER BY hour ASC')
            last = db.fetchmany()

            if check_hour == last[0][1] and check_min == last[0][2]:

                con.execute("DELETE FROM Alarms WHERE hour = ? and minute = ?", (check_hour, check_min))
                con.commit()

                return True
            else:
                return False

        except Exception as e:
            return False


def get_alarms():
    with sqlite3.connect("Oracle") as con:
        try:
            db = con.execute('SELECT * FROM Alarms ORDER BY hour ASC')
            alarms = db.fetchall()
            print(alarms)

            if alarms is None:
                return False

            return alarms

        except Exception as e:
            return False


def delete_alarms():

    with sqlite3.connect("Oracle") as con:
        try:

            print("deleting")
            con.execute("DELETE FROM Alarms ")
            con.commit()

            return True

        except Exception as e:
            return False



