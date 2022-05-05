import logging

from datetime import datetime
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from tg_bot.keyboards.inline import days_scroll
from tg_bot.test_data.test_timetable_data import test_timetable_data
from tg_bot.text_format.timetable_text import format_timetable_text


class Day:
    weekType = test_timetable_data["actualWeekType"]
    weekDay = datetime.isoweekday(datetime.today())


async def display_timetable(message: Message):
    await message.answer(text=format_timetable_text(Day.weekType, Day.weekDay),
                         reply_markup=days_scroll,
                         parse_mode="HTML")


def register_timetable(dp: Dispatcher):
    dp.register_message_handler(display_timetable,
                                commands=["timetable"],
                                state="*")


async def scroll_previous_day(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    if Day.weekDay == 1:
        Day.weekType = 2 if Day.weekType == 1 else 1
        Day.weekDay = 7
    else:
        Day.weekDay -= 1

    await call.message.edit_text(text=format_timetable_text(Day.weekType, Day.weekDay),
                                 parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_pr_day(dp: Dispatcher):
    dp.register_callback_query_handler(scroll_previous_day,
                                       text=["scroll_pr_day"])


async def scroll_next_day(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    if Day.weekDay == 7:
        Day.weekType = 2 if Day.weekType == 1 else 1
        Day.weekDay = 1
    else:
        Day.weekDay += 1

    await call.message.edit_text(text=format_timetable_text(Day.weekType, Day.weekDay),
                                 parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_next_day(dp: Dispatcher):
    dp.register_callback_query_handler(scroll_next_day,
                                       text=["scroll_next_day"])


async def change_week(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    Day.weekType = 2 if Day.weekType == 1 else 1
    await call.message.edit_text(text=format_timetable_text(Day.weekType, Day.weekDay),
                                 parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_change_week(dp: Dispatcher):
    dp.register_callback_query_handler(change_week,
                                       text=["change_week"])
