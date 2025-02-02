import json
import os

import aiohttp
import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.buttons.reply_buttons import back_main_menu_button, main_menu_buttons, brands_button, service_button, \
    spare_parts_button
from bot.buttons.support_functions import check_brand, check_spare_part
from bot.buttons.text import back_main_menu, back_main_menu_ru, car_ru, car, truck, truck_ru, special, special_ru, \
    spare_part_text_ru, spare_part_text, service_text, service_text_ru
from bot.dispatcher import dp, bot
from main import admins


# @dp.message_handler(Text(equals=[contact, contact_ru]))
# async def contact_function(msg: types.Message):
#     if msg.text == contact:
#         await msg.answer(text='Yagona telefon raqami: +998912787878')
#     else:
#         await msg.answer(text='Единственный номер телефона: +998912787878')
#
#
# @dp.message_handler(Text(equals=[social_networks, social_networks_ru]))
# async def sociable_networks_function(msg: types.Message):
#     if msg.text == social_networks:
#         await msg.answer(text="""
# Bizning ijtimoiy tarmoqlarga obuna bo'ling 👇:
#
# Instagram: https://www.instagram.com/arzon.lab/
# YouTube: https://youtube.com/@arzonlab
# Facebook: https://www.facebook.com/profile.php?id=61558339262051
# Telegram: https://t.me/arzonlab""")
#     else:
#         await msg.answer(text="""
# Подписывайтесь на наши социальные сети 👇:
#
# Instagram: https://www.instagram.com/arzon.lab/
# YouTube: https://youtube.com/@arzonlab
# Facebook: https://www.facebook.com/profile.php?id=61558339262051
# Telegram: https://t.me/arzonlab""")
#
#
# @dp.message_handler(Text(equals=[ask_question, ask_question_ru]))
# async def ask_question_function(msg: types.Message, state: FSMContext):
#     await state.set_state('ask_question')
#     if msg.text == ask_question:
#         await msg.answer(
#             text="Talab va istaklaringizni yozib qoldiring va biz albatta ko'rib chiqib yechim topishga harakat qilamiz:",
#             reply_markup=await back_main_menu_button(msg.from_user.id))
#     else:
#         await msg.answer(text="Запишите ваши требования и пожелания и мы обязательно постараемся найти решение:",
#                          reply_markup=await back_main_menu_button(msg.from_user.id))
#
#
# @dp.message_handler(state='ask_question')
# async def receive_question_and_notify_admins(msg: types.Message, state: FSMContext):
#     user_info = f"User ID: <a href='tg://user?id={msg.from_user.id}'>{msg.from_user.id}</a>\n" \
#                 f"Username: @{msg.from_user.username}\n" \
#                 f"Ism-Familiya: {msg.from_user.full_name}\n" \
#                 f"Xabar: {msg.text}"
#     for admin in admins:
#         await bot.send_message(chat_id=admin, text=user_info, parse_mode='HTML')
#     tg_user = json.loads(
#         requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{msg.from_user.id}/").content)
#     if tg_user['language'] == 'uz':
#         await msg.answer(text="Xabaringiz adminlarga jo'natildi!",
#                          reply_markup=await main_menu_buttons(msg.from_user.id))
#     else:
#         await msg.answer(text="Ваше сообщение отправлено администраторам!",
#                          reply_markup=await main_menu_buttons(msg.from_user.id))
#     await state.finish()

@dp.message_handler(Text(equals=[car, car_ru, truck, truck_ru, special, special_ru]))
async def car_function_1(msg: types.Message, state: FSMContext):
    await state.set_state('choose_brand')
    if msg.text == car or msg.text == truck or msg.text == special:
        await msg.answer(text="Markani tanlang 👇",
                         reply_markup=await brands_button(chat_id=msg.from_user.id, type=msg.text))
    else:
        await msg.answer(text="Выберите бренд 👇",
                         reply_markup=await brands_button(chat_id=msg.from_user.id, type=msg.text))


@dp.message_handler(state="choose_brand")
async def car_function_2(msg: types.Message, state: FSMContext):
    brand_status = await check_brand(msg.text)
    async with state.proxy() as data:
        if brand_status == 0:
            await msg.answer(text="Markalarni tugmalar orqali tanlang 👇",
                             reply_markup=await brands_button(chat_id=msg.from_user.id, type=data["type"]))
            return
        data['brand'] = msg.text
    await state.set_state("choose_service")
    text, button = await service_button(msg.from_user.id)
    await msg.answer(text=text, reply_markup=button)


@dp.message_handler(Text(equals=[spare_part_text, spare_part_text_ru, service_text, service_text_ru]),
                    state="choose_service")
async def car_function_3(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if msg.text in [spare_part_text, spare_part_text_ru]:
            data['service'] = spare_part_text
        else:
            data['service'] = service_text
    await state.set_state("choose_part")
    text, button = await spare_parts_button(msg.from_user.id)
    await msg.answer(text=text, reply_markup=button)


@dp.message_handler(state="choose_part")
async def car_function_4(msg: types.Message, state: FSMContext):
    part_status = await check_spare_part(msg.text)
    async with state.proxy() as data:
        pass
    if part_status == 0:
        text, button = await spare_parts_button(msg.from_user.id)
        await msg.answer(text="Ehtiyot qisimni tugmalar orqali tanlang 👇",
                         reply_markup=button)
        return
    tg_user = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{msg.from_user.id}/").content
    )
    contacts = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/api/contacts/filter/{data['brand']}/{msg.text}/").content
    )
    if tg_user['language'] == 'uz':
        for contact in contacts['results']:
            await msg.answer(text=f"""
Tashkilot nomi: {contact['name']}
Manzil: {contact['address']}
Orientir: {contact['landmark']}
Telefon raqam: {contact['phone_number']}
""")
        await state.finish()
        await msg.answer(text=f"Sizning so'rovingiz bo'yicha {contacts['count']} ta tashkilot topildi ☝",
                         reply_markup=await main_menu_buttons(msg.from_user.id))
    else:
        for contact in contacts['results']:
            await msg.answer(text=f"""
Названия организация: {contact['name']}
Адрес: {contact['address']}
Ориентир: {contact['landmark']}
Телефон номер: {contact['phone_number']}
""")
        await state.finish()
        await msg.answer(text=f"По вашему запросу найдено {contacts['count']} организаций ☝",
                         reply_markup=await main_menu_buttons(msg.from_user.id))
