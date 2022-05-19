import logging

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from tg_bot.keyboards.inline import teacher_scroll
from tg_bot.dialog_states.teacher_info_search_state import TeacherDialog
from tg_bot.text_format.teacher_info_text import find_all_teachers, \
    format_timetable_text
from tg_bot.users import users, User


async def display_teachers(message: Message, state: FSMContext):
    answer = message.text
    user = message.from_user.id

    if user not in users:
        users[user] = User(teacher_name=answer,
                           teachers=find_all_teachers(answer))
    else:
        users[user].teacher_name = answer
        users[user].teachers = find_all_teachers(answer)
        users[user].teacher_number = 0

    await state.finish()

    if not users[user].teachers:
        await message.answer(text=f"Преподаватель не найден",
                             parse_mode="HTML")

    elif len(users[user].teachers) == 1:
        teacher_number = users[user].teacher_number
        await message.answer(text=format_timetable_text(users[user].teachers[teacher_number]),
                             parse_mode="HTML")

    else:
        teacher_number = users[user].teacher_number
        await message.answer(text=format_timetable_text(users[user].teachers[teacher_number]),
                             reply_markup=teacher_scroll,
                             parse_mode="HTML")


def register_display_teachers(dp: Dispatcher):
    dp.register_message_handler(display_teachers,
                                state=TeacherDialog.answer)


async def ask_teacher(message: Message):
    await message.answer(text="Введите ФИО (или часть) преподавателя",
                         parse_mode="HTML")

    await TeacherDialog.answer.set()


def register_ask_teacher(dp: Dispatcher):
    dp.register_message_handler(ask_teacher,
                                commands=["teacher_info"],
                                state="*")


async def scroll_previous_teacher_info(call: CallbackQuery):
    await call.answer(cache_time=1)
    user = call.from_user.id

    callback_data = call.data

    logging.info(f"{callback_data=}")

    if users[user].teacher_number == 0:
        users[user].teacher_number = len(users[user].teachers) - 1
    else:
        users[user].teacher_number -= 1

    teacher_number = users[user].teacher_number
    await call.message.edit_text(text=format_timetable_text(users[user].teachers[teacher_number]),
                                 parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=teacher_scroll)


def register_previous_teacher_info(dp: Dispatcher):
    dp.register_callback_query_handler(scroll_previous_teacher_info,
                                       text=["scroll_previous_teacher_info"])


async def scroll_next_teacher_info(call: CallbackQuery):
    await call.answer(cache_time=1)
    user = call.from_user.id

    callback_data = call.data

    logging.info(f"{callback_data=}")

    if users[user].teacher_number == len(users[user].teachers) - 1:
        users[user].teacher_number = 0
    else:
        users[user].teacher_number += 1

    teacher_number = users[user].teacher_number
    await call.message.edit_text(text=format_timetable_text(users[user].teachers[teacher_number]),
                                 parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=teacher_scroll)


def register_next_teacher_info(dp: Dispatcher):
    dp.register_callback_query_handler(scroll_next_teacher_info,
                                       text=["scroll_next_teacher_info"])


def register_full_teacher_info(dp: Dispatcher):
    register_display_teachers(dp)
    register_ask_teacher(dp)
    register_previous_teacher_info(dp)
    register_next_teacher_info(dp)
