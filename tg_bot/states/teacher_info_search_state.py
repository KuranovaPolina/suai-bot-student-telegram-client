from aiogram.dispatcher.filters.state import State, StatesGroup


class TeacherDialog(StatesGroup):
    answer = State()
