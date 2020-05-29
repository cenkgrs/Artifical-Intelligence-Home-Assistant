import sqlite3
import logging

logger = logging.Logger('catch_all')


def user_info():
    age = int(input('What is your age: '))
    gender = input('What is your gender: ')
    weight = int(input('What is your weight: '))
    height = int(input('What is your height in inches: '))

    if gender == 'male':
        c1 = 66
        hm = 6.2 * height
        wm = 12.7 * weight
        am = 6.76 * age
    elif gender == 'female':
        c1 = 655.1
        hm = 4.35 * height
        wm = 4.7 * weight
        am = 4.7 * age

    bmr_result = c1 + hm + wm - am

    return int(bmr_result)


def calculate_activity(activity_level, bmr_result):
    if activity_level == 'none':
        activity_level = 1.2 * bmr_result
    elif activity_level == 'light':
        activity_level = 1.375 * bmr_result
    elif activity_level == 'moderate':
        activity_level = 1.55 * bmr_result
    elif activity_level == 'heavy':
        activity_level = 1.725 * bmr_result
    elif activity_level == 'extreme':
        activity_level = 1.9 * bmr_result

    return int(activity_level)


def gain_or_lose(activity_level, goals):
    if goals == 'lose':
        calories = activity_level - 500
    elif goals == 'maintain':
        calories = activity_level
    elif goals == 'gain':
        gain = 1
        if gain == 1:
            return activity_level + 500
        elif gain == 2:
            return activity_level + 1000


def result(gender, height, weight, age, activity_level, goals):
    if gender == 'male':
        c1 = 66
        hm = 6.2 * (float(height) / 2.54)
        wm = 12.7 * int(weight)
        am = 6.76 * int(age)
    elif gender == 'female':
        c1 = 655.1
        hm = 4.35 * height
        wm = 4.7 * weight
        am = 4.7 * age

    bmr_result = c1 + hm + wm - am

    activity = calculate_activity(activity_level, bmr_result)

    calories = gain_or_lose(activity, goals)

    protein = calculate_protein(activity_level, weight, goals)

    carb = int((calories / 2) / 4)

    fat = calculate_fat(activity_level, goals, calories)

    print(protein, carb, fat)
    insert_cal(calories, protein, carb, fat, gender, int(height), int(weight), int(age), activity_level, goals)

    return check_cal()


def calculate_protein(activity_level, weight, goals):
    if goals == 'lose':
        goal_multiplier = -0.2
    elif goals == 'maintain':
        goal_multiplier = 0
    else:  # gain
        goal_multiplier = 0.4

    if activity_level == 'none':
        protein = (1.2 + goal_multiplier) * int(weight)
    elif activity_level == 'light':
        protein = (1.4 + goal_multiplier) * int(weight)
    elif activity_level == 'moderate':
        protein = (1.7 + goal_multiplier) * int(weight)
    elif activity_level == 'heavy':
        protein = (1.9 + goal_multiplier) * int(weight)
    elif activity_level == 'extreme':
        protein = (2.1 + goal_multiplier) * int(weight)

    return int(protein)


def calculate_fat(activity_level, goals, calories):
    if goals == 'lose':
        goal_multiplier = -0.07
    elif goals == 'maintain':
        goal_multiplier = 0
    else:  # gain
        goal_multiplier = 0.07

    if activity_level == 'none':
        fat = (calories * (0.25 + goal_multiplier)) / 10
    elif activity_level == 'light':
        fat = (calories * (0.26 + goal_multiplier)) / 10
    elif activity_level == 'moderate':
        fat = (calories * (0.27 + goal_multiplier)) / 10
    elif activity_level == 'heavy':
        fat = (calories * (0.28 + goal_multiplier)) / 10
    elif activity_level == 'extreme':
        fat = (calories * (0.29 + goal_multiplier)) / 10

    return int(fat)


def insert_cal(calories, protein, carb, fat, gender, height, weight, age, activity_level, goals):
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO person_diets (calories, protein, carb, fat,  gender, height, weight, age, "
                           "activity_level, goal) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
                           (calories, protein, carb, fat, gender, height, weight, age, activity_level, goals))
            con.commit()

            return True

        except Exception as e:
            logger.error('Error: ' + str(e))
            return False


def check_cal():
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()

        try:
            data = cursor.execute("SELECT * FROM person_diets WHERE id = (SELECT MAX(id) FROM person_diets)")
            data = data.fetchone()

            if data:
                kcal = data[1]
                prot = data[2]
                carb = data[3]
                fat = data[4]

                return {"kcal": kcal, "prot": prot, "carb": carb, "fat": fat}
            else:
                return False

        except Exception as e:
            logger.error('Error: ' + str(e))
            return False
