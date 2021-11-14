# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.button import add_case
from loader import dp
from states.state import AddCase


@dp.message_handler(text='Добавить портфель 💼')
async def bot_start(message: types.Message):
    await message.answer(f"Вы можете добавить свой сводный портфель в виде csv файла\n"
                         f"Или посмотреть возможности сервиса на тестовам портфеле🙃", reply_markup=add_case)

