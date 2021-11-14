# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Справка 📜"),
        ],
        [
            KeyboardButton(text="Добавить портфель 💼"),
        ]

    ],
    resize_keyboard=True
)


add_case = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить свой потрфель 💼"),
        ],
        [
            KeyboardButton(text="Добавить тестовый портфель 🧳"),
        ]

    ],
    resize_keyboard=True
)
risk_prifile = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Консервативный 🥸"),
            KeyboardButton(text="Умеренный 😶"),
            KeyboardButton(text="Рискованный 🤯")
        ]

    ],
    resize_keyboard=True
)

choise_func = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Аналитика инструментов")
        ],
        [
            KeyboardButton(text="Рекомендации по портфелю")
        ]

    ],
    resize_keyboard=True
)
graf = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📈 График цены акции 📈")
        ],
        [
            KeyboardButton(text="📈 График изменения цены акции 📈")
        ],
        [
            KeyboardButton(text="Рекомендации по портфелю")
        ]

    ],
    resize_keyboard=True
)