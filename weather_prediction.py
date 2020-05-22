import pandas as pd
from sklearn import preprocessing
import sklearn
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import pickle
import sklearn.model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# This function for getting natural language value of predicted condition value
def get_condition_value(index):
    data = pd.read_csv("csv/Istanbul Weather Data.csv", sep=",")

    conditions = sorted(set(sorted(list(data["Condition"]))))
    return conditions[index[0]]


# This function prepares date values
def prepare_date():
    date_data = []
    data = pd.read_csv("csv/Istanbul Weather Data.csv", sep=",")

    dates = list(data["DateTime"])

    for date in dates:
        day = date.split(".")[0]
        month = date.split(".")[1]

        date_data.append(day + "." + month)

    return date_data


# This function prepares sun rise and sun set values
def prepare_hours():
    data = pd.read_csv("csv/Istanbul Weather Data.csv", sep=",")

    sunrise = []
    sunset = []

    rise = data["SunRise"]
    set = data["SunSet"]

    # Split two hour to pieces and get hour, minute to get float value
    for r_hour, s_hour in zip(rise, set):
        r_hour, s_hour = r_hour.split(":"), s_hour.split(":")
        sunrise.append(float(str(r_hour[0] + "." + str(r_hour[1]))))
        sunset.append(float(str(s_hour[0] + "." + str(s_hour[1]))))

    return sunrise, sunset


# This function prepares data for to split
def prepare_data():
    data = pd.read_csv("csv/Istanbul Weather Data.csv", sep=",")
    le = preprocessing.LabelEncoder()

    date_data = prepare_date()
    min_temp = data["MinTemp"]
    max_temp = data["MaxTemp"]

    sun_rise, sun_set = prepare_hours()

    wind = data["AvgWind"]
    humidity = data["AvgHumidity"]
    pressure = data["AvgPressure"]

    condition = le.fit_transform(list(data["Condition"]))

    test_target = list(zip(date_data, min_temp, max_temp, sun_rise, sun_set, wind, humidity, pressure))

    prepare_test_train_data(test_target, condition)


# This function takes test data and predict target and splits for train and test
def prepare_test_train_data(test_target, predict_target):
    X = test_target
    y = list(predict_target)

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    train_model(x_train, x_test, y_train, y_test)


# This function train model and save it for to use at predictions
def train_model(x_train, x_test, y_train, y_test):
    new_model = KNeighborsClassifier(n_neighbors=1)

    new_model.fit(x_train, y_train)
    acc = new_model.score(x_test, y_test)

    print(acc)

    with open("models/weather_condition.pickle", "wb") as f:
        pickle.dump(new_model, f)

    predictions = new_model.predict(x_test)
    for x in range(len(predictions)):
        print("Predicted: ", predictions[x], "Data: ", x_test[x], "Actual: ", y_test[x])


def predict_max_temp(date_data, min_temp, sun_rise, sun_set, wind, humidity, pressure):
    test = [(date_data, min_temp, sun_rise, sun_set, wind, humidity, pressure)]
    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("models/weather_temp_1.pickle", "rb")
    model = pickle.load(pickle_in)

    return int(model.predict(test)[0])


def predict_min_temp(date_data, max_temp, sun_rise, sun_set, wind, humidity, pressure):
    test = [(date_data, max_temp, sun_rise, sun_set, wind, humidity, pressure)]
    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("models/weather_min_temp.pickle", "rb")
    model = pickle.load(pickle_in)

    return int(model.predict(test)[0])


def predict_wind(date_data, min_temp, max_temp, sun_rise, sun_set, humidity, pressure):
    test = [(date_data, min_temp, max_temp, sun_rise, sun_set, humidity, pressure)]
    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("models/weather_wind.pickle", "rb")
    model = pickle.load(pickle_in)

    return int(model.predict(test)[0])


def predict_condition(date_data, min_temp, max_temp, sun_rise, sun_set, wind, humidity, pressure):
    test = [(date_data, min_temp, max_temp, sun_rise, sun_set, wind, humidity, pressure)]
    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("models/weather_condition.pickle", "rb")
    model = pickle.load(pickle_in)

    predicted_data = model.predict(test)

    result = get_condition_value(predicted_data)

    return result


def get_predictions(weather_data):
    predicted_condition = predict_condition(weather_data["date"], weather_data["temp_min"], weather_data["temp_max"],
                                            weather_data["sunrise"], weather_data["sunset"], weather_data["wind"],
                                            weather_data["humidity"], weather_data["pressure"])

    predicted_max_temp = predict_max_temp(weather_data["date"], weather_data["temp_min"],
                                          weather_data["sunrise"], weather_data["sunset"], weather_data["wind"],
                                          weather_data["humidity"], weather_data["pressure"])

    predicted_min_temp = predict_min_temp(weather_data["date"], weather_data["temp_max"],
                                          weather_data["sunrise"], weather_data["sunset"], weather_data["wind"],
                                          weather_data["humidity"], weather_data["pressure"])

    predicted_wind = predict_max_temp(weather_data["date"], weather_data["temp_min"], weather_data["temp_max"],
                                      weather_data["sunrise"], weather_data["sunset"],
                                      weather_data["humidity"], weather_data["pressure"])

    data = [{"condition": predicted_condition, "max_temp": predicted_max_temp,
            "min_temp": predicted_min_temp, "wind": predicted_wind}]

    return data

# x_train, x_test, y_train, y_test = prepare_data()
# train_model(x_train, x_test, y_train, y_test)

# res = predict_max_temp('26.05', 17,  5.45, 20.22,  17, 71, 1021)
# predict_min_temp('24.05', 20,  5.45, 20.22, 28, 30, 1021)
