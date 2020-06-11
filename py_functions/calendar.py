from datetime import datetime
import sqlite3
import config

month_number = datetime.now().month
month = config.months[month_number]


def add_calendar_info(inputs):
    print(inputs)
    info = inputs["text"]
    day = inputs["day"]

    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO calendar (info, day, month)"
                           "VALUES (?, ?, ?) ", (info, day, month))

            return True, ""
        except sqlite3.OperationalError:
            return False, "Couldn't set the calendar sir"


def get_calendar_info():

    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()

        try:
            db = cursor.execute("SELECT info, day FROM calendar WHERE month = ?", (month,))
            informations = db.fetchall()

            return informations, ""
        except sqlite3.OperationalError:
            return None, "Couldn't get the calendar informations sir"

