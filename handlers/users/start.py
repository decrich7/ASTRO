# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.button import start_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет 👋, {message.from_user.full_name}!\n"
                         f"ASTRO - Это сервис позволяющий провести аналитику и рекомендации для сводного портфел"
                         f"я\n"
                         f'Чтобы узнать больше информации о возможностях сервиса нажмите на кнопку "Справка 📜"', reply_markup=start_button)
