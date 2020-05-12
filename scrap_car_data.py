from bs4 import BeautifulSoup
from requests import get
import pandas as pd

content_list = []
prices = []
page_num=1

base_url = f"https://www.cars.com/for-sale/searchresults.action/?page={page_num}&perPage=100&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=34110"

print(base_url)
while page_num < 3:

    response = get(base_url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    content_list += html_soup.find_all('span', attrs={'class': 'listing-row__price '})
    print(content_list)


    page_num += 1
    base_url = f"https://www.cars.com/for-sale/searchresults.action/?page={page_num}&perPage=100&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=34110"

for x in content_list:
    print(x.text)
    prices.append((((x.text).replace("$", "")).replace(" ", "")).replace("\n", ""))

print(prices)



