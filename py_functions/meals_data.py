import sqlite3
import datetime
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from flask import jsonify
from word2number import w2n
from scrap_meal_list import get_vegetable_data, get_fruit_data
import pickle

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"]

stop_words = set(stopwords.words('english'))

with open("fruits.txt", "rb") as fp:  # Unpickling
    fruits = pickle.load(fp)

with open("vegetables.txt", "rb") as fp:  # Unpickling
    vegetables = pickle.load(fp)


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
            # Get inserted meals from morning, afternoon and evening
            db = cursor.execute("Select meal From meals Where meal_time = ? and date = ?", ("morning", date,))
            data[0]["morning"] = db.fetchall()

            db = cursor.execute("Select meal From meals Where meal_time = ? and date = ?", ("afternoon", date,))
            data[0]["afternoon"] = db.fetchall()

            db = cursor.execute("Select meal From meals Where meal_time = ? and date = ?", ("evening", date,))
            data[0]["evening"] = db.fetchall()

            # Get total nutrition of the inserted meals
            db = cursor.execute("Select sum(kcal) as kcal, sum(carb) as carb, sum(prot) as prot, sum(fat) as fat"
                                " From meals Where date = ?", (date,))
            nutritions = db.fetchall()

            # Place nutrition values to dictionary object
            data[0]["nutrition"]["kcal"] = nutritions[0][0]
            data[0]["nutrition"]["carb"] = nutritions[0][1]
            data[0]["nutrition"]["prot"] = nutritions[0][2]
            data[0]["nutrition"]["fat"]  = nutritions[0][3]

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


def add_meal_natural(text):
    no_number = False
    meals = []
    meal_time = ""

    text = text["text"]
    date = str(datetime.date.today())

    text_backup = text.split(" ")

    # Get meal time from text_backup
    for i in text_backup:
        if i == "morning" or i == "afternoon" or i == "evening":
            meal_time = i

    # If meal time not specified return error
    if meal_time == "":
        return False, "expected-meal-time"

    # Get meals from text_backup
    for index, item in enumerate(text_backup):
        # Get the quantity and meal after it and add it to meals
        if item in numbers:
            number = numbers.index(item)
            meal = str(number) + " " + text_backup[index + 1]
            meals.append(meal)

    # If meals list empty ( there wasn't any number in list) -> get meals from txt files
    if not meals:
        no_number = True
        text_tokens = word_tokenize(text)

        # Filtering text so there will be less loop
        filtered_sentence = [w for w in text_tokens if not w in stop_words]

        # remove meal time from text
        filtered_sentence.remove(meal_time)

        # Add meal to meals list if any
        for item in filtered_sentence:
            if item in fruits or item in vegetables:
                meals.append(item)

    # Add meals list items to database
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        for meal in meals:
            meal_gram = 75
            try:
                print(meal)
                quantity = 1
                # If there was no numbers in text -> meaning meals got from the txt files
                if not no_number:
                    quantity = (meal.split(" "))[0]
                    meal = (meal.split(" "))[1]

                db = cursor.execute("Select * From recipes Where name = ?", (meal,))

                # If there is no record of this meal in database continue to next meal
                if not db:
                    continue
                data = db.fetchall()

                meal_gram = float(meal_gram) / 100  # For using the gr value to get exact nutrition values of the foods
                # Get the nutrition values of the current meal
                kcal = data[0][2] * (meal_gram * int(quantity))
                carb = data[0][3] * (meal_gram * int(quantity))
                prot = data[0][4] * (meal_gram * int(quantity))
                fat = data[0][5] * (meal_gram * int(quantity))
                print(kcal, carb, prot, fat)

                # Add current meal to meals table with nutrition values
                cursor.execute("INSERT INTO meals (date, meal_time, meal, kcal, carb, prot, fat) "
                               "VALUES (?, ?, ?, ?, ?, ?, ?) ", (date, meal_time, meal, kcal, carb, prot, fat))

                con.commit()

                continue
            except sqlite3.OperationalError:
                continue

    return True, "no error"
