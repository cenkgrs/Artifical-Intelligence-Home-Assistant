import sqlite3
import datetime


def add_meal(meal, meal_time, meal_id, meal_gram):
    date = str(datetime.date.today())

    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            db = cursor.execute("Select * From recipes Where id = ?", (meal_id,))
            data = db.fetchall()
            print(data)
            print(data[0])
            meal_gram = float(meal_gram) / 100  # For using the gr value to get exact nutrition values of the foods

            kcal = data[0][2] * meal_gram
            carb = data[0][3] * meal_gram
            prot = data[0][4] * meal_gram
            fat = data[0][5] * meal_gram
            print(kcal, carb, prot, fat)
            if meal_time == "morning":
                cursor.execute("INSERT INTO meals (date, meal_time, meal, kcal, carb, prot, fat) "
                               "VALUES (?, ?, ?, ?, ?, ?, ?) ", (date, meal_time, meal, kcal, carb, prot, fat))

            con.commit()

            return True
        except sqlite3.OperationalError:
            return False


def get_meals():
    date = str(datetime.date.today())

    data = [{"morning": '', "afternoon": '', 'evening': '', "nutrition": {"kcal": '', "carb": '', "prot": '', "fat": ''}}]
    date = str(datetime.date.today())
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()

        try:
            db = cursor.execute("Select meal From meals Where meal_time = ?", ("morning",))
            data[0]["morning"] = db.fetchall()

            db = cursor.execute("Select meal From meals Where meal_time = ?", ("afternoon",))
            data[0]["afternoon"] = db.fetchall()

            db = cursor.execute("Select meal From meals Where meal_time = ?", ("evening",))
            data[0]["evening"] = db.fetchall()

            db = cursor.execute("Select sum(kcal) as kcal, sum(carb) as carb, sum(prot) as prot, sum(fat) as fat"
                                " From meals Where date = ?", (date,))
            nutritions = db.fetchall()
            print(nutritions[0])
            data[0]["nutrition"]["kcal"] = nutritions[0][0]
            data[0]["nutrition"]["carb"] = nutritions[0][1]
            data[0]["nutrition"]["prot"] = nutritions[0][2]
            data[0]["nutrition"]["fat"]  = nutritions[0][3]

            print(data[0]["nutrition"])
            return data
        except sqlite3.OperationalError:
            return False


def get_meal_input(inp):
    with sqlite3.connect("Oracle") as con:
        try:
            cursor = con.cursor()

            db = cursor.execute("Select * From recipes Where name Like ?",
                                (inp + '%',))
            if not db:
                return False

            data = db.fetchall()
            return data
        except sqlite3.OperationalError:
            return False
