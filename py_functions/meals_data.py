import sqlite3
import datetime


def add_meal(meal, meal_time):
    date = str(datetime.date.today())

    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            if meal_time == "morning":
                cursor.execute("INSERT INTO meals (date, meal_time, meal) VALUES (?, ?, ?) ", (date, meal_time, meal))

            elif meal_time == "evening":
                cursor.execute("INSERT INTO meals (date, meal_time, meal) VALUES (?, ?, ?) ", (date, meal_time, meal))

            elif meal_time == "afternoon":
                cursor.execute("INSERT INTO meals (date, meal_time, meal) VALUES (?, ?, ?) ", (date, meal_time, meal))

            con.commit()

            return True
        except sqlite3.OperationalError:
            return False


def get_meals():
    data = [{"morning": '', "afternoon": '', 'evening': ''}]
    date = str(datetime.date.today())
    print("meals")
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()

        try:
            db = cursor.execute("Select meal From meals Where meal_time = ?", ("morning",))
            data[0]["morning"] = db.fetchall()

            db = cursor.execute("Select meal From meals Where meal_time = ?", ("afternoon",))
            data[0]["afternoon"] = db.fetchall()

            db = cursor.execute("Select meal From meals Where meal_time = ?", ("evening",))
            data[0]["evening"] = db.fetchall()

            return data
        except sqlite3.OperationalError:
            return False


def get_meal_input(inp):
    with sqlite3.connect("Oracle") as con:
        try:
            cursor = con.cursor()
            print("got here")
            print(inp)
            db = cursor.execute("Select * From recipes Where name Like ?",
                                (inp + '%',))
            if not db:
                return False

            data = db.fetchall()
            return data
        except sqlite3.OperationalError:
            return False
