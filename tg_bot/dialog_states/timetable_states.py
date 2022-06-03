from aiogram.dispatcher.filters.state import State, StatesGroup


class TimetableDialog(StatesGroup):
    group_number = State()
