import json
import time
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from models import Animal
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from sqlalchemy.orm import Session
from models import engine
import asyncio
import aiohttp
from sqlalchemy.orm import sessionmaker

link = 'https://less-homeless.com/find-your-best-friend-today/page/1/'

def cook_soup(link):
    headers = Headers(browser='chrome', os='win')
    req = requests.get(link, headers=headers.generate())
    time.sleep(2)
    soup = BeautifulSoup(req.text, 'lxml')
    cards = soup.find_all('div', class_='card zs_card')
    return cards


def parsed_data(cards):
    for card in cards:
        pet_link= card.find('a', class_='card__title w-inline-block').get('href') # Ссылка на питомца
        pet_img = card.find('div', class_='lazyload card__image').get('data-bg') # Блок с картинкой
        pet_age = card.find('div', class_='card__value').text
        pet_name = card.find('h2').text  # Имя питомца
        sex = card.find('div', class_='card__value').text  # пол питомца



# def parsing():
#     with Session(engine) as session:
#         for card in cards:
#             a_tag = card.find('a', class_='card__title w-inline-block')  # Ссылка на питомца
#             img_div = card.find('div', class_='lazyload card__image').text  # Блок с картинкой
#             name_tag = card.find('h2').text  # Имя питомца
#             sex = card.find('div', class_='card__value').text  # пол питомца
#             animal = Animal(name=name_tag, age=1, sex=sex, photo_url=img_div,
#                             description='one')
#             session.add(animal)
#             session.commit()


