# -*- coding: utf-8 -*-
import os
from aiogram import types
from aiogram.types import InputFile
import asyncio
from aiogram.dispatcher import FSMContext
from analysis import Analysis
from recomend import Rec
from aiogram.dispatcher.filters.builtin import CommandStart
from states.state import AddCase
from grafik import Price, PriceIzm
from keyboards.default.button import choise_func, graf
from loader import dp, bot
from states.state import ChoiseRisk
from states.state import Func


@dp.message_handler(state=Func.func)
async def risk(message: types.Message, state: FSMContext):
    if message.text == 'Аналитика инструментов':
        an = Analysis('shares.csv', 1)
        text = '✅ Цена акций на данный момент:\n    {}\n\n' \
               '✅ Cредняя годовая доходность:\n    {}\n\n' \
               '✅ Дивидентный доход:\n    {}\n\n' \
               '✅ Цена акций:\n    {}\n\n' \
               '✅ Стоимость портфеля:\n    {}$\n\n' \
               '✅ Ожидаемая годовая прибыль портфеля:\n    {}%\n\n' \
               '✅ Годовая волатильность портфеля:\n    {}%\n\n' \
               '✅ Коэффициент Шарпа портфеля:\n    {}\n\n'

        list_price = []
        for b, t in an.brokers.items():
            list_price.append(f'<b>{b}:</b>')
            list_price += [f'<b>{an.names[i]}</b>  -  <em>{round(an.prise_stock()[i], 3)}$</em>' for i in t]

        list_annual_profit = []
        for b, t in an.brokers.items():
            list_annual_profit.append(f'<b>{b}:</b>')
            list_annual_profit += [f'<b>{an.names[i]}</b>  -  <em>{round(an.annual_profit()[i], 4)}%</em>'
                                   for i in t]

        dividend_profit = []
        for b, t in an.brokers.items():
            dividend_profit.append(f'<b>{b}:</b>')
            dividend_profit += [f'<b>{an.names[i]}</b>  -  <em>{round(an.dividend_profit()[i], 4)}%</em>'
                                for i in t]

        price_all_shares = []
        for b, t in an.brokers.items():
            price_all_shares.append(f'<b>{b}:</b>')
            price_all_shares += [f'<b>{an.names[i]}</b>  -  <em>{round(an.price_all_shares()[i], 3)}$</em>'
                                 for i in t]

        await message.answer(text.format('\n    '.join(list_price),
                          '\n    '.join(list_annual_profit),
                          '\n    '.join(dividend_profit),
                          '\n    '.join(price_all_shares),
                          an.price_briefcase(),
                          *an.performance_briefcase()), reply_markup=graf)

    elif message.text == 'Рекомендации по портфелю':
        data = await state.get_data()
        risk = data.get("risk")
        r = Rec(str(risk).split()[0])
        text = f'✅ Количество акций в портфеле\n' \
               f'    {r.fin_stock()}\n\n' \
               f'✅ Ожидаемая годовая прибыль:\n' \
               f'    До - {r.profit_year()[0]}    После - {r.profit_year()[1]}\n\n' \
               f'✅ Годовая волатильность:\n' \
               f'    До - {r.volatility_year()[0]}    После - {r.volatility_year()[1]}\n\n' \
               f'✅ Коэффициент Шарпа:\n' \
               f'    До - {r.koef_sharp()[0]}    После - {r.koef_sharp()[1]}\n\n' \
               f'✅ Остаток средств\n' \
               f'    {r.balance()}'
        await message.answer(text, reply_markup=choise_func)

    elif message.text == '📈 График цены акции 📈':
        p = Price()
        p.get_graf()
        await asyncio.sleep(1)
        photo = InputFile(path_or_bytesio="график.png")  # Local file
        await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption="Здесь указаны графики цен акций вашего портфеля 💼")

    elif message.text == '📈 График изменения цены акции 📈':
        count = 0
        pz = PriceIzm()
        pz.get_graf_all()
        await asyncio.sleep(1)
        while True:
            await asyncio.sleep(0.5)
            try:
                photo = InputFile(path_or_bytesio=f"график{count}.png")  # Local file
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo=photo,
                                     caption="")
            except:
                break
            count += 1
