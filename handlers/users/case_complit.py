# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.state import AddCase

from keyboards.default.button import risk_prifile
from loader import dp
from states.state import ChoiseRisk


@dp.message_handler(text='Добавить тестовый портфель 🧳', state=None)
async def bot_start(message: types.Message):
    await message.answer('Супер! Вы сразу же можете опробовать все возможности нашего сервиса😊\n'
                         'Сводный портфель содержит следующие инструменты:\n'
                         '<strong>broker   name   tickers   count   date</strong>\n\n'
                         '<em>Тинькофф Инвестиции   Apple Inc   AAPL   12   2020-12-05</em>\n\n'
                         '<em>Тинькофф Инвестиции   General Electric Company   GE   123   2020-11-13</em>\n\n'
                         '<em>Альфа-Директ   Bank Of America Corp   BAC   23   2020-12-10</em>\n\n'
                         '<em>Тинькофф Инвестиции   Advanced Micro Devices Inc   AMD   42   2020-11-17</em>\n\n'
                         '<em>Альфа-Директ   Plug Power Inc   PLUG   155   2020-12-20</em>\n\n'
                         '<em>Альфа-Директ   Ford Motor Company   F   42   2020-12-22</em>\n\n')
    await message.answer('Теперь вам следует указать риск-профиль для сводного портфеля 💹\n'
                         'Вот основные типы риск-профилей 🔎\n'
                         '<strong>Консервативный</strong> - <em>Где цель инвестора сохранить капитал и защитить его от инфляции</em>\n\n'
                         '<strong>Умеренный</strong> - <em>Инвестор готов принять незначительный риск ради потенциальной доходности</em>\n\n'
                         '<strong>Агрессивный</strong> - <em>Приоритет такого инвестора — максимальная доходность</em>\n\n'
                         'Выберите один из профилей 🤓', reply_markup=risk_prifile)
    await ChoiseRisk.risk.set()
    # await state.finish()


@dp.message_handler(text='Добавить свой потрфель 💼')
async def bot_start(message: types.Message):
    await message.answer('Отлично!😁\n'
                         'В файле должны быть следующие колонки\n'
                         '<strong>name  tickers   count   date</strong>\n'
                         'name - Название акции\n'
                         'tickers - Уникальным идентификатор акции\n'
                         'count - Количество купленных акций\n'
                         'date - Дата покупки\n')
    # await AddCase.case.set()
