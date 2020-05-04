import sqlite3
import datetime


def add_todo_item(date, todo):

    if date == "today":
        date = str(datetime.date.today())
    elif date == "tomorrow":
        date = str(datetime.date.today() + datetime.timedelta(days=1))
    else:
        date = date

    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO todo (date, todo) VALUES (?, ?) ", (date, todo))

            con.commit()

            return True
        except sqlite3.OperationalError:
            return False


def get_todo():
    data = [{"today": '', "tomorrow": ''}]
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            today = str(datetime.date.today())
            db = cursor.execute("Select todo From todo Where date = ?", (today,))
            data[0]["today"] = db.fetchall()

            tomorrow =  str( datetime.date.today() + datetime.timedelta(days=1))
            db = cursor.execute("Select todo From todo Where date = ?", (tomorrow,))
            data[0]["tomorrow"] = db.fetchall()

            return data
        except sqlite3.OperationalError:
            return False
