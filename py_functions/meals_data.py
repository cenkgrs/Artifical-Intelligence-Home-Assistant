import sqlite3
import datetime
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle
import logging
from json_files.recipes import recipe_list


logger = logging.Logger('catch_all')

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
           "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
           "sixteen", "seventeen", "eighteen", "nineteen"]

stop_words = set(stopwords.words('english'))

# I'm getting the fruits and vegetables data from the pickle file that i fill with web scrapping
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

            if not data:
                return False

            meal_gram = float(meal_gram) / 100  # For using the gr value to get exact nutrition values of the foods

            kcal = data[0][2] * meal_gram
            prot = data[0][3] * meal_gram
            carb = data[0][4] * meal_gram
            fat = data[0][5] * meal_gram

            cursor.execute("INSERT INTO meals (date, meal_time, meal, kcal, carb, prot, fat) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?) ", (date, meal_time, meal, kcal, carb, prot, fat))

            con.commit()

            return True
        except sqlite3.OperationalError:
            return False


# This is for getting meal records and total nutrition values of today
def get_meals():
    date = str(datetime.date.today())

    data = [
        {"morning": '', "afternoon": '', 'evening': '', "nutrition": {"kcal": '', "carb": '', "prot": '', "fat": ''},
         "needs": {"prot": '', "carb": '', "fat": ''}}
    ]

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
            data[0]["nutrition"]["fat"] = nutritions[0][3]

            db = cursor.execute("SELECT * FROM person_diets WHERE id = (SELECT MAX(id) FROM person_diets)")
            needs = db.fetchone()

            if needs is not None:
                data[0]["needs"]["kcal"] = needs[1]
                data[0]["needs"]["prot"] = needs[2]
                data[0]["needs"]["carb"] = needs[3]
                data[0]["needs"]["fat"] = needs[4]

            return data
        except sqlite3.OperationalError:
            return False


# This functions get the meal records like user typed and returns similar records
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


# This function is for getting meal record with speech recognition
def add_meal_natural(text):
    print(text)
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

                data = db.fetchall()
                print(data)

                if not data:
                    continue

                meal_gram = float(meal_gram) / 100  # For using the gr value to get exact nutrition values of the foods
                # Get the nutrition values of the current meal
                kcal = data[0][2] * (meal_gram * int(quantity))
                prot = data[0][3] * (meal_gram * int(quantity))
                carb = data[0][4] * (meal_gram * int(quantity))
                fat = data[0][5] * (meal_gram * int(quantity))
                print(kcal, prot, carb, fat)

                # Add current meal to meals table with nutrition values
                cursor.execute("INSERT INTO meals (date, meal_time, meal, kcal, carb, prot, fat) "
                               "VALUES (?, ?, ?, ?, ?, ?, ?) ", (date, meal_time, meal, kcal, carb, prot, fat))

                con.commit()

                continue
            except sqlite3.OperationalError:
                continue

    return True, "no error"


# This algorithm finds a fit meal for that hour and returns its recipe to user
def get_meal_recommendation():
    hour = datetime.datetime.now().hour

    # Multiplier is for getting the current needs meaning on morning you should get 1000 cal at afternon you must
    # have total 2000 cal and at evening total 2800 cal Time multiplier for getting only that hour's nutritions needs
    # -> at evening you should get 800 cal
    if 12 > hour >= 6:
        time = "morning"
        multiplier = 0.35
        time_multiplier = 0.35
    else:
        time = "evening"
        multiplier = 1
        time_multiplier = 0.30
        if 18 > hour >= 12:
            time = "afternoon"
            multiplier = 0.70
            time_multiplier = 0.35

    # if hour > 23 or hour <= 5:
    #   return "You shouldn't eat anything at this hour sir", False

    recipes = check_needs_left(multiplier, time_multiplier)

    if recipes:
        return recipes, True

    return "I couldn't find any recipe for you sir", False


# This function will return difference of what user ate and how much more should user eat ( by nutrition grams )
def check_needs_left(multiplier, time_multiplier):
    date = str(datetime.date.today())
    daily_needs = []

    # Time needs is nutrition needs for meals to that hour
    # Meaning you must have eaten 2000 cal at the end of this hour
    # ( afternoon etc -> 1000 cal at morning, 1000cal at afternoon total 2000 cal)
    time_needs = []

    daily_currents = []

    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()

        try:
            db = cursor.execute("SELECT * FROM person_diets WHERE id = (SELECT MAX(id) FROM person_diets)")
            needs = db.fetchone()

            db = cursor.execute("Select sum(kcal) as kcal, sum(prot) as prot, sum(carb) as carb, sum(fat) as fat"
                                " From meals Where date = ?", (date,))
            nutritions = db.fetchone()

        except Exception as e:
            logger.error('Error: ' + str(e))
            return False

        # Daily needs for user
        if needs is not None:
            for i in range(1, 5):
                daily_needs.append(needs[i])
                time_needs.append(needs[i] * multiplier)  # This is the needs for that hour (morning, evening etc)

        # If nothing eaten yet make all values 0 for error handling
        if nutritions[0] is None:
            nutritions = [0] * 4

        # Today's eaten food's nutrition
        for i in range(0, 4):
            daily_currents.append(nutritions[i])

        return get_difference(daily_needs, daily_currents, time_needs, time_multiplier, multiplier)


def get_difference(target, current, time_needs, time_multiplier, multiplier):
    nutrition_names = ["kcal", "prot", "carb", "fat"]

    # These list represent how much difference between what user ate and how much should eat -> in percentange
    differences = []

    # These list represent how much nutrition deficits user has for that hour (morning, evening)
    deficits = []

    # TR -> kalori açığı o öğünde alabileceğinden fazlaysa max öğün miktarını al değilse açığı al ( 2500 cal aldım
    # 300 cal daha almam lazım gibi ) If cal deficit is larger than what user can get at this hour set cal_defiticit

    # to max user can get at this hour Meaning if there is a 1600 cal deficit at the moment -> user can get 800 cal
    # at this hour so cal_deficit is 800 cal

    for index, item in enumerate(target):
        if current[index] > target[index] * multiplier:
            return "You shouldn't eat any more food right now sir", False

        deficit = target[index] * time_multiplier if ((target[index] * multiplier) - current[index]) > (target[index] * time_multiplier) else target[index] * multiplier
        deficits.append(deficit)

    # This loop for finding in what type user did get the least nutrition and max
    # So we can find what should user be predominantly fed at -> like protein or cal
    for index, item in enumerate(target):
        differences.append(current[index] / item)

    max_diff = max(differences)  # What user should eat least
    min_diff = min(differences)  # What user should eat most

    max_index = differences.index(max_diff)
    max_type = nutrition_names[max_index]

    min_index = differences.index(min_diff)
    min_type = nutrition_names[min_index]  # Return value like fat, cal

    # After getting this deficits and max differences we can search food like -> food that has large cal
    # and not have any fat because user filled the fat level

    return get_best_fit_recipes(deficits, min_type, max_type)


def get_best_fit_recipes(deficits, min_type, max_type):

    best_fit_recipes = []

    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()

        try:
            db = cursor.execute("SELECT * FROM "
                                "(SELECT * FROM recipes ORDER BY " + min_type + " DESC LIMIT 5)"
                                "ORDER BY " + max_type + " ASC LIMIT 5 ")
            recipes = db.fetchall()

            # This loop finds similarity score for every recipe found
            # user need 400 cal so 300 cal -> recipe has 0.75 cal_similarity point
            # If recipe nutrition value is higher than what user needs, recipe wont get point for that nutrition
            # For every 100 cal higher than it should returns -0.1 point for that recipe,
            # for other nutritions(carb, fat) its 10 gr higher

            for recipe in recipes:

                cal_similarity = recipe[2] / deficits[0] if recipe[2] <= deficits[0] else (deficits[0] - recipe[2]) * 0.001
                prot_similarity = recipe[3] / deficits[1] if recipe[3] <= deficits[1] else (deficits[1] - recipe[3]) * 0.01
                carb_similarity = recipe[4] / deficits[2] if recipe[4] <= deficits[2] else (deficits[2] - recipe[4]) * 0.01
                fat_similarity = recipe[5] / deficits[3] if recipe[5] <= deficits[3] else (deficits[3] - recipe[5]) * 0.01

                similarity_score = cal_similarity + prot_similarity + carb_similarity + fat_similarity

                # Create list of dictionaries for best fit recipes
                recipe = {"name": recipe[1], "similarity_score": similarity_score}
                best_fit_recipes.append(recipe)

            # Sort recipes by similarity score
            best_fit_recipes = sorted(best_fit_recipes, key = lambda i: i['similarity_score'], reverse=True)

            recipe_count = 0
            recipes = []

            for fit_recipe in best_fit_recipes:
                for recipe_item in recipe_list:

                    if fit_recipe["name"] == recipe_item["name"]:
                        recipe_count += 1
                        recipes.append(recipe_item)
                        continue

                    if recipe_count == 3:
                        break

            return recipes

        except Exception as e:
            logger.error('Error: ' + str(e))
            return False
