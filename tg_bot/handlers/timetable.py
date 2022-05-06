import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from tg_bot.keyboards.inline import days_scroll
from tg_bot.text_format.timetable_text import format_timetable_text
from tg_bot.users import users, User, Day


async def display_timetable(message: Message):
    user = message.from_user.id

    if user not in users:
        users[user] = User(Day())
    else:
        users[user].user_day = Day()

    print(user)
    print(users)
    await message.answer(text=format_timetable_text(users[user].user_day.week_type,
                                                    users[user].user_day.week_day),
                         reply_markup=days_scroll,
                         parse_mode="HTML")


def register_timetable(dp: Dispatcher):
    dp.register_message_handler(display_timetable,
                                commands=["timetable"],
                                state="*")


async def scroll_previous_day(call: CallbackQuery):
    await call.answer(cache_time=1)
    user = call.from_user.id
    print(user)
    callback_data = call.data

    logging.info(f"{callback_data=}")

    if users[user].user_day.week_day == 1:
        users[user].user_day.week_type = 2 if users[user].user_day.week_type == 1 else 1
        users[user].user_day.week_day = 7
    else:
        users[user].user_day.week_day -= 1

    await call.message.edit_text(text=format_timetable_text(users[user].user_day.week_type,
                                                            users[user].user_day.week_day),
                                 parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_previous_day(dp: Dispatcher):
    dp.register_callback_query_handler(scroll_previous_day,
                                       text=["scroll_previous_day"])


async def scroll_next_day(call: CallbackQuery):
    await call.answer(cache_time=1)
    user = call.from_user.id
    print(user)
    callback_data = call.data

    logging.info(f"{callback_data=}")

    if users[user].user_day.week_day == 7:
        users[user].user_day.week_type = 2 if users[user].user_day.week_type == 1 else 1
        users[user].user_day.week_day = 1
    else:
        users[user].user_day.week_day += 1

    await call.message.edit_text(text=format_timetable_text(users[user].user_day.week_type,
                                                            users[user].user_day.week_day),
                                 parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_next_day(dp: Dispatcher):
    dp.register_callback_query_handler(scroll_next_day,
                                       text=["scroll_next_day"])


async def change_week(call: CallbackQuery):
    await call.answer(cache_time=1)
    user = call.from_user.id
    print(user)
    callback_data = call.data

    logging.info(f"{callback_data=}")

    users[user].user_day.week_type = 2 if users[user].user_day.week_type == 1 else 1
    await call.message.edit_text(text=format_timetable_text(users[user].user_day.week_type,
                                                            users[user].user_day.week_day),
                                 parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_change_week(dp: Dispatcher):
    dp.register_callback_query_handler(change_week,
                                       text=["change_week"])


def register_full_timetable(dp: Dispatcher):
    register_timetable(dp)
    register_previous_day(dp)
    register_next_day(dp)
    register_change_week(dp)
