import csv
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model, preprocessing
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import HashingVectorizer
import sys

from tensorflow.compiler.tf2xla.python.xla import le

'''file = open("texts/texts.txt", "r")
doclist = [ line for line in file ]
docstr = '' . join(doclist)
sentences = re.split(r'[\n]', docstr)

print(sentences)'''

with open('texts/texts.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    print(stripped)
    lines = (line.split(",") for line in stripped if line)
    with open('test.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('text', 'command'))
        writer.writerows(lines)

data = pd.read_csv("test.csv", sep=",")

le = preprocessing.LabelEncoder()
texts = le.fit_transform(list(data["text"]))
commands = le.fit_transform(list(data["command"]))
predict = "command"
predictions = ["thanks", "greeting", "goodness", "checking"]
texts = list(data["text"])
commands = list(data["command"])
X = list(zip(texts))
Y = list(zip(commands))


vectorizer = HashingVectorizer(n_features=20)

for i in X:
    vectorX = vectorizer.transform(i)
    vectorX.toarray()
for i in Y:
    vectorY = vectorizer.transform(i)
    vectorY.toarray()

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

X = np.array(vectorX, dtype=object)
Y = np.array(vectorY, dtype=object)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)


model = KNeighborsClassifier(n_neighbors=4)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    print("Predicted: ", predicted[x], "Data: ", x_test[x], "Actual: ", y_test[x])