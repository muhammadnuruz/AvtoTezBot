import json

import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.buttons.text import back_main_menu, adverts, none_advert, forward_advert, choice_language, choice_language_ru, \
    back_main_menu_ru, car, truck, \
    special, truck_ru, car_ru


async def main_menu_buttons(chat_id: int):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{chat_id}/").content)
    if tg_user['language'] == 'uz':
        design = [
            [car, truck, special],
            [choice_language]
        ]
    else:
        design = [
            [car_ru, truck_ru, special],
            [choice_language_ru]
        ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_main_menu_button(chat_id: int):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{chat_id}/").content)
    if tg_user['language'] == 'uz':
        design = [[back_main_menu]]
    else:
        design = [[back_main_menu_ru]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def brands_button(chat_id: int, type: str):
    tg_user = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{chat_id}/").content
    )
    user_language = tg_user.get("language", "uz")
    brands = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/api/brands/filter/{type}").content
    )
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = []
    for brand in brands['results']:
        button = KeyboardButton(text=brand['name'])
        buttons.append(button)

    for i in range(0, len(buttons), 2):
        keyboard.row(*buttons[i:i + 2])

    if user_language == 'uz':
        keyboard.add(back_main_menu)
    else:
        keyboard.add(back_main_menu_ru)

    return keyboard


async def admin_menu_buttons():
    design = [
        [adverts],
        [back_main_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def advert_menu_buttons():
    design = [
        [none_advert, forward_advert],
        [back_main_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
