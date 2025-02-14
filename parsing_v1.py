import json
import time

import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

link = 'https://less-homeless.com/'
headers = Headers(browser='chrome', os='win')
req = requests.get(link, headers=headers.generate())
time.sleep(2)
soup = BeautifulSoup(req.text, 'lxml')
# results = soup.find_all('section', class_='main-special-case block width-1240')
results = soup.find_all('div', class_='special_case__card')

headers = []

for res in results:
    header = res.find("div", class_="special_case__title").text
    headers.append(header)
print(headers)
