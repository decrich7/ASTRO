from aiogram.dispatcher.filters.state import StatesGroup, State


class AddCase(StatesGroup):
    case = State()


class ChoiseRisk(StatesGroup):
    risk = State()


class Func(StatesGroup):
    func = State()
