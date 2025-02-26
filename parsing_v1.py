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
'''DATABASE_URL в models'''


def find_cards():
    page_num = 1
    all_cards = []

    while page_num < 15:
        link = f'https://less-homeless.com/find-your-best-friend-today/page/{page_num}/'
        print(page_num)
        headers = Headers(browser='chrome', os='win')
        req = requests.get(link, headers=headers.generate())
        time.sleep(2)
        soup = BeautifulSoup(req.text, 'lxml')
        cards = soup.find_all('div', class_='card zs_card')
        page_num +=1
        if not cards:
            break
        all_cards.extend(cards)

    return all_cards


def parsed_data(cards):
    with Session(engine) as session:
        for card in cards:
            pet_link= card.find('a', class_='card__title w-inline-block').get('href') # Ссылка на питомца
            pet_img = card.find('div', class_='lazyload card__image').get('data-bg') # Блок с картинкой
            pet_age = card.find('div', class_='card__value').text
            pet_name = card.find('h2').text  # Имя питомца
            sex = card.find('div', class_='card__value').text  # пол питомца
            animal = Animal(name=pet_name, age=pet_age, sex=sex, photo_url=pet_img,
                            description=pet_link)
            session.add(animal)
            session.commit()

parsed_data(find_cards())




