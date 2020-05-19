import re

patterns = []


text = "i ate 1 banana and 2 apple at morning"
text = text.split(" ")
print(text)

for index, item in enumerate(text):
    if item.isnumeric():

        meal = str(index) + " " + text[index + 1]
        print(meal)