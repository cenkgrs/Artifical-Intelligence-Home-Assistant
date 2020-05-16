import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import preprocessing
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style


def get_brand_index(val):
    data = pd.read_csv("csv/car-data.csv")
    le = preprocessing.LabelEncoder()

    brands = sorted(set(sorted(list(data["brand"]))))

    try:
        return brands.index(val)
    except ValueError:
        return False


def get_transmission_index(val):
    transmissions = ["Automanual", "Automatic", "CVT", "Manual"]
    try:
        return transmissions.index(val)
    except ValueError:
        return False


def train_model(x_train, x_test, y_train, y_test):
    new_model = KNeighborsClassifier(n_neighbors=10)

    new_model.fit(x_train, y_train)
    acc = new_model.score(x_test, y_test)

    print(acc)

    with open("car_price_model_1.pickle", "wb") as f:
        pickle.dump(new_model, f)


def prepare_data():
    data = pd.read_csv("csv/car-data_1.csv")

    le = preprocessing.LabelEncoder()
    brand = le.fit_transform(list(data["brand"]))
    years = list(data["years"])
    mileage = list(data["mileage"])
    transmission = le.fit_transform(list(data["transmission"]))
    price = list(data["price"])

    X = list(zip(brand, years, mileage, transmission))
    y = list(price)

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    return x_train, x_test, y_train, y_test


def predict(brand, year, mileage, transmission):
    brand = get_brand_index(brand)
    transmission = get_transmission_index(transmission)
    print(brand, transmission)

    if not brand:
        return False, "brand"
    elif not transmission:
        return False, "transmission"

    test = [(brand, year, mileage, transmission)]

    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("car_price_model.pickle", "rb")
    model = pickle.load(pickle_in)

    predicted_data = model.predict(test)
    print(predicted_data)

    return predicted_data, False


def test_predict(x_test, y_test):
    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("car_price_model_1.pickle", "rb")
    model = pickle.load(pickle_in)

    predictions = model.predict(x_test)
    for x in range(len(predictions)):
        print("Predicted: ", predictions[x], "Data: ", x_test[x], "Actual: ", y_test[x] )


'''x_train, x_test, y_train, y_test = prepare_data()
train_model(x_train, x_test, y_train, y_test)

test_predict(x_test, y_test)'''

#predict("Audi", 2020, 50000, "Manual")







