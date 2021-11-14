# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from states.state import AddCase

from keyboards.default.button import choise_func
from loader import dp
from states.state import ChoiseRisk
from states.state import Func


@dp.message_handler(state=ChoiseRisk.risk)
async def risk(message: types.Message, state: FSMContext):
    await state.update_data(
        {"risk": message.text}
    )
    # data = await state.get_data()
    await message.answer(
        'Теперь вы можете посмотреть аналитику и рекомендации по портфелю исходя из указанного профиля риска 🧐',
        reply_markup=choise_func)
    await Func.func.set()
    # await state.finish()