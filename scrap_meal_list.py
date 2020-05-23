from bs4 import BeautifulSoup
from requests import get
import re
import pickle

fruits = []
vegetables = []
meals = []


def get_fruit_data():

    fruit_list = []
    base_url = "https://edis.ifas.ufl.edu/topic_fruit_and_nut_index"

    response = get(base_url)
    html_soup = BeautifulSoup(response.text, "html.parser")

    div = html_soup.find('div',  class_=['content-main-fixed-width'])

    for ultag in div.find_all('ul'):
        for litag in ultag.find_all('li'):
            fruit = re.sub('\n', '', litag.text).lstrip(" ")
            fruit, sep, tail = fruit.partition(" ")
            fruits.append(fruit.lower())

    with open("fruits.txt", "wb") as fp:  # Pickling
        pickle.dump(fruits, fp)

    return fruits


def get_vegetable_data():

    vegetable_items = []

    url = "https://www.enchantedlearning.com/wordlist/vegetables.shtml"

    response = get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")

    vegetable_items = html_soup.find_all('div',  class_=["wordlist-item"])

    for vegetable in vegetable_items:
        vegetables.append(vegetable.text.lower())

    with open("vegetables.txt", "wb") as fp:  # Pickling
        pickle.dump(vegetables, fp)

    return vegetables


def get_meal_data():

    meal_items = []

    url = "https://www.tasteofhome.com/collection/classic-comfort-food-dinners/"

    response = get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")

    meal_items = html_soup.find_all("a", class_=["no-smoothstate"])

    for meal in meal_items:
        print(meal)


get_fruit_data()
get_vegetable_data()