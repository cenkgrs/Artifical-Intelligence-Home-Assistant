import pandas as pd
from sklearn import preprocessing
import sklearn
from sklearn.neighbors import KNeighborsClassifier
import pickle
import math
from sklearn.model_selection import train_test_split
import sklearn.model_selection


def get_from():
    new_dates = []
    data = pd.read_csv("csv/sleepdata.csv", sep=";")

    le = preprocessing.LabelEncoder()

    start_dates = list(data["Start"])

    for i in start_dates:
        date = i.split(" ")  # Will seperate date and time
        date = date[1].split(":")  # Will seperate time
        date = date[0]  # Will get hour from time

        new_dates.append(int(date))

    #start_hours = le.fit_transform(list(new_dates))

    start_hours = new_dates
    print("lenght:" , len(start_hours))

    return start_hours


def get_to():
    new_dates = []
    data = pd.read_csv("csv/sleepdata.csv", sep=";")

    le = preprocessing.LabelEncoder()

    start_dates = list(data["End"])

    for i in start_dates:
        date = i.split(" ")  # Will seperate date and time
        date = date[1].split(":")  # Will seperate time
        date = date[0]  # Will get hour from time

        new_dates.append(int(date))

    #end_hours = le.fit_transform(list(new_dates))

    end_hours = new_dates

    print("lenght:" , len(end_hours))

    return end_hours


def get_sleep_time():
    sleep_times = []
    data = pd.read_csv("csv/sleepdata.csv", sep=";")
    le = preprocessing.LabelEncoder()

    times = list(data["Time in bed"])

    for i in times:
        hour = i.replace(":", ".")  # Converts 8:32 to 8.32
        hour = round(float(hour))  # Converts 8.32 to 8 or 8.65 to 9 (Rounds the hour)
        sleep_times.append(hour)

    return sleep_times


def get_sleep_quality():
    sleep_qualitys = []
    data = pd.read_csv("csv/sleepdata.csv", sep=";")

    quality = list(data["Sleep quality"])

    for i in quality:
        qual = int(i.replace("%", ""))
        qual = int(round(qual, -1))

        sleep_qualitys.append(qual)

    return sleep_qualitys


def get_wake_up_status():
    data = pd.read_csv("csv/sleepdata.csv", sep=";")
    le = preprocessing.LabelEncoder()

    quality = list(data["Sleep quality"])
    times = list(data["Time in bed"])
    status = list(data["Wake up"])

    for index, stat in enumerate(status):
        if pd.isna(stat):
            qual = quality[index]
            qual = int(qual.replace("%", ""))  # Convert 78% this to this 78

            hour = times[index].replace(":", ".")  # Converts 8:32 to 8.32
            hour = round(float(hour))

            if qual < 50 and hour < 5:
                status[index] = ":|"
                continue
            elif qual < 50 and hour > 5:
                status[index] = ":)"
                continue
            elif qual > 50 and hour < 5:
                status[index] = ":|"
                continue
            elif qual > 75 and 3 <= hour <= 5:
                status[index] = ":)"
                continue
            elif qual >= 59 and hour > 5:
                status[index] = ":)"
                continue

            status[index] = ":|"
    status = list(status)

    print("lenght:" , len(status))

    return status


def prepare_data():
    start_hours = get_from()
    end_hours = get_to()
    sleep_times = get_sleep_time()
    sleep_qualitys = get_sleep_quality()
    wake_status = get_wake_up_status()

    X = list(zip(start_hours, end_hours, sleep_qualitys, sleep_times))
    y = list(wake_status)

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    return x_train, x_test, y_train, y_test


def train_model(x_train, x_test, y_train, y_test):
    new_model = KNeighborsClassifier(n_neighbors=10)

    new_model.fit(x_train, y_train)
    acc = new_model.score(x_test, y_test)

    print(acc)

    with open("models/sleep_habits_2.pickle", "wb") as f:
        pickle.dump(new_model, f)

    predictions = new_model.predict(x_test)
    for x in range(len(predictions)):
        print("Predicted: ", predictions[x], "Data: ", x_test[x], "Actual: ", y_test[x])


def predict(bedtime, get_up, quality, sleep_time):

    test = [(bedtime, get_up, quality, sleep_time)]
    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("models/sleep_habits_2.pickle", "rb")
    model = pickle.load(pickle_in)

    predicted_data = model.predict(test)

    if predicted_data == ':)':
        return 1
    else:
        return 0


def test_predict(x_test, y_test):
    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("models/sleep_habits_2.pickle", "rb")
    model = pickle.load(pickle_in)

    predictions = model.predict(x_test)
    for x in range(len(predictions)):
        print("Predicted: ", predictions[x], "Data: ", x_test[x], "Actual: ", y_test[x] )


# x_train, x_test, y_train, y_test = prepare_data()
# train_model(x_train, x_test, y_train, y_test)
# test_predict(x_test, y_test)

# test_data = [('03', '04', 10, 1)]
# predict(1, 9, 75, 8)