from bs4 import BeautifulSoup
import requests
import pyttsx3
import lxml
import random
import speech_recognition as sr
import webbrowser
import os
import re

url = "https://www.google.com/search?ei=el-HXvqxIoukgweZ3KCQAw&q=batman"

links = []
to_remove = []
clean_links = []

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'lxml')

results = soup.find_all("div", attrs = {"ZINbbc"} )
for r in results:
    try:
        link = r.find('a', href=True)

        if link != '':
            links.append(link['href'])

    except:
        continue

for i, l in enumerate(links):
    clean = re.search('\/url\?q\=(.*)\&sa', l)

    # Anything that doesn't fit the above pattern will be removed
    if clean is None:
        to_remove.append(i)
        continue
    clean_links.append(clean.group(1))

print(clean_links[0])