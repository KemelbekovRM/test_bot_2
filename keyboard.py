# опишем пару кнопок

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

button_privet = KeyboardButton('Салям уалейкум,\n как тебя зовут?')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_privet)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_privet)
