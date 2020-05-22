import pandas as pd
from sklearn import preprocessing
import sklearn
from sklearn.neighbors import KNeighborsClassifier
import pickle
import sklearn.model_selection


def prepare_date():
    date_data = []
    data = pd.read_csv("csv/Istanbul Weather Data.csv", sep=",")

    dates = list(data["DateTime"])

    for date in dates:
        day = date.split(".")[0]
        month = date.split(".")[1]

        date_data.append(day + "." + month)

    return date_data


def prepare_hours():
    data = pd.read_csv("csv/Istanbul Weather Data.csv", sep=",")

    sunrise = []
    sunset = []

    rise = data["SunRise"]
    for i in rise:
        sunrise.append(float(i))

    print(rise)


def prepare_data():
    data = pd.read_csv("csv/Istanbul Weather Data.csv", sep=",")
    le = preprocessing.LabelEncoder()

    date_data = prepare_date()
    print(date_data)
    min_temp = data["MinTemp"]
    max_temp = data["MaxTemp"]

    sun_rise = le.fit_transform(data["SunRise"])
    sun_set = le.fit_transform(data["SunSet"])

    wind = data["AvgWind"]
    humidity = data["AvgHumidity"]
    pressure = data["AvgPressure"]

    X = list(zip(date_data, le.fit_transform(data["Condition"]), sun_rise, sun_set,  wind, humidity, pressure))
    y = list(max_temp)

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    return x_train, x_test, y_train, y_test


def train_model(x_train, x_test, y_train, y_test):
    new_model = KNeighborsClassifier(n_neighbors=2)

    new_model.fit(x_train, y_train)
    acc = new_model.score(x_test, y_test)

    print(acc)

    with open("models/weather_temp.pickle", "wb") as f:
        pickle.dump(new_model, f)

    predictions = new_model.predict(x_test)
    for x in range(len(predictions)):
        print("Predicted: ", predictions[x], "Data: ", x_test[x], "Actual: ", y_test[x])


def predict(bedtime, get_up, quality, sleep_time):

    test = [(bedtime, get_up, quality, sleep_time)]
    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("models/weather_temp.pickle", "rb")
    model = pickle.load(pickle_in)

    predicted_data = model.predict(test)

    if predicted_data == ':)':
        return 1
    else:
        return 0


x_train, x_test, y_train, y_test = prepare_data()
train_model(x_train, x_test, y_train, y_test)

#prepare_hours()