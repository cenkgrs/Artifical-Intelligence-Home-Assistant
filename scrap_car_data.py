from bs4 import BeautifulSoup
from requests import get
import pandas as pd

prices = []
mileages = []
page_num = 1

car = {
    "price": "",
    "mileage": "",
    "year": "",
    "brand": "",
}

prices_list = []
mileages_list = []
titles_list = []

base_url = f"https://www.cars.com/for-sale/searchresults.action/?page={page_num}&perPage=100&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=34110"

print(base_url)
while page_num < 2:

    response = get(base_url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    prices_list += html_soup.find_all('span', attrs={'class': 'listing-row__price '})
    mileages_list += html_soup.find_all('span', attrs={'class': 'listing-row__mileage'})
    titles_list += html_soup.find_all('span', attrs={'class': 'listing - row__title'})

    page_num += 1
    base_url = f"https://www.cars.com/for-sale/searchresults.action/?page={page_num}&perPage=100&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=34110"

    for x in mileages_list:
        mile = float((((x.text.replace("mi.", "")).replace(" ", "")).replace("\n", "")).replace(",", "."))
        km = mile * 1.609
        mileages.append(km)
    for x in prices_list:
        prices.append(((x.text.replace("$", "")).replace(" ", "")).replace("\n", ""))

print(len(prices))
print(len(mileages))


