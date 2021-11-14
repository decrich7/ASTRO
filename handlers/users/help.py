from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = 'Какой функционал имеет сервис ASTRO 🧐\n\n' \
           'Мы предоставляем аналитику и рекомендации по сводному портфелю\n' \
           'Что входит в аналитику:\n\n' \
           '   <strong>1) Цена акции на данный момент</strong>\n' \
           '   <strong>2) Средняя годовая доходность по каждой акции</strong>\n' \
           '   <strong>3) Дивидентный доход для каждой акции</strong>\n' \
           '   <strong>4) Цена акций(цена * кол-во)</strong>\n' \
           '   <strong>5) Цена портфеля</strong>\n\n' \
           'Что входит в Рекомендации к портфелю:\n\n' \
           '   <strong>1) Портфель пересобирается исходя из указанного риск профиля</strong>\n' \
           '   <strong>2) Ожидаемая годовая прибыль портфеля</strong>\n' \
           '   <strong>3) Годовая волатильность портфеля</strong>\n' \
           '   <strong>4) Коэффициент Шарпа(отношение прибыли к риску)</strong>\n' \
           '   <strong>5) Остаток средств</strong>'
    
    await message.answer(text)


@dp.message_handler(text='Справка 📜')
async def bot_help(message: types.Message):
    text = 'Какой функционал имеет сервис ASTRO 🧐\n\n' \
           'Мы предоставляем аналитику и рекомендации по сводному портфелю\n' \
           'Что входит в аналитику:\n\n' \
           '   <strong>1) Цена акции на данный момент</strong>\n' \
           '   <strong>2) Средняя годовая доходность по каждой акции</strong>\n' \
           '   <strong>3) Дивидентный доход для каждой акции</strong>\n' \
           '   <strong>4) Цена акций(цена * кол-во)</strong>\n' \
           '   <strong>5) Цена портфеля</strong>\n\n' \
           'Что входит в Рекомендации к портфелю:\n\n' \
           '   <strong>1) Портфель пересобирается исходя из указанного риск профиля</strong>\n' \
           '   <strong>2) Ожидаемая годовая прибыль портфеля</strong>\n' \
           '   <strong>3) Годовая волатильность портфеля</strong>\n' \
           '   <strong>4) Коэффициент Шарпа(отношение прибыли к риску)</strong>\n' \
           '   <strong>5) Остаток средств</strong>'

    await message.answer(text)
