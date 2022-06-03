from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('/timetable'),
    KeyboardButton('/teacher_info')
)
