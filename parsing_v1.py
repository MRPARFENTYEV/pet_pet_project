import json
import time

import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

# link = 'https://less-homeless.com/'
link = 'https://less-homeless.com/find-your-best-friend-today/'
headers = Headers(browser='chrome', os='win')
req = requests.get(link, headers=headers.generate())
time.sleep(2)
soup = BeautifulSoup(req.text, 'lxml')

cards = soup.find_all('div', class_ = 'card zs_card')
# results = soup.find_all('div', class_='special_case__card')
# print(card)
headers = []
#
for card in cards:
    a_tag = card.find('a', class_='card__title w-inline-block')  # Ссылка на питомца
    img_div = card.find('div', class_='lazyload card__image')  # Блок с картинкой
    name_tag = card.find('h2')  # Имя питомца
    sex = card.find('div',class_='card__value').text
    print(sex)

    if a_tag and 'href' in a_tag.attrs and img_div and 'data-bg' in img_div.attrs:
        pet_name = name_tag.text.strip() if name_tag else "Неизвестно"
        pet_url = a_tag['href']
        image_url = img_div['data-bg']
        # print('url!',pet_url)
        # print('pet_name!',pet_name)
        # print('image_url',image_url)

#     header = res.find("div", class_="special_case__title").text

#     headers.append(header)
# print(headers)
