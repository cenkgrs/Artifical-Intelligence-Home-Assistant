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
    data = pd.read_csv("car-data.csv")
    le = preprocessing.LabelEncoder()

    brands = sorted(set(sorted(list(data["brand"]))))
    return brands.index(val)


def train_model(x_train, x_test, y_train, y_test):
    new_model = KNeighborsClassifier(n_neighbors=5)

    new_model.fit(x_train, y_train)
    acc = new_model.score(x_test, y_test)

    print(acc)

    with open("car_price_model.pickle", "wb") as f:
        pickle.dump(new_model, f)


def prepare_data():
    data = pd.read_csv("car-data.csv")

    le = preprocessing.LabelEncoder()
    brand = le.fit_transform(list(data["brand"]))
    years = list(data["years"])
    mileage = list(data["mileage"])
    transmission = le.fit_transform(list(data["transmission"]))
    price = list(data["price"])

    X = list(zip(brand, years, mileage, transmission))
    y = list(price)

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    return x_test, y_test


def predict(test, x_test, y_test):
    # This will open saved model and put it inside model variable( that ill use for predict)
    pickle_in = open("car_price_model.pickle", "rb")
    model = pickle.load(pickle_in)

    predicted_data = model.predict(test)
    print(predicted_data)

    predictions = model.predict(x_test)
    for x in range(len(predictions)):
        print("Predicted: ", predictions[x], "Data: ", x_test[x], "Actual: ", y_test[x] )


x_test, y_test = prepare_data()

index = get_brand_index("Ferrari")
test_data = [(28, 2019, 15000, 1)]
predict(test_data, x_test, y_test)





