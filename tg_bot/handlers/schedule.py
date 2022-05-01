import logging

from datetime import datetime
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from tg_bot.keyboards.inline import days_scroll
from tg_bot.test_schedule_data import test_schedule_data
from tg_bot.creating_formatted_text import schedule_text


class Day:
    weekType = test_schedule_data["actual_week_type"]
    weekDay = datetime.weekday(datetime.today())


async def schedule_schedule(message: Message):
    await message.answer(text=schedule_text(Day.weekType, Day.weekDay),
                         reply_markup=days_scroll, parse_mode="HTML")


def register_schedule(dp: Dispatcher):
    dp.register_message_handler(schedule_schedule,
                                commands=["schedule"],
                                state="*")


async def previous_day(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    if Day.weekDay == 0:
        Day.weekType = 1 if Day.weekType == 0 else 0
        Day.weekDay = 6
    else:
        Day.weekDay -= 1

    await call.message.edit_text(text=schedule_text(Day.weekType, Day.weekDay))
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_pr_day(dp: Dispatcher):
    dp.register_callback_query_handler(previous_day, text=["pr_day"])


async def next_day(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    if Day.weekDay == 6:
        Day.weekType = 1 if Day.weekType == 0 else 0
        Day.weekDay = 0
    else:
        Day.weekDay += 1

    await call.message.edit_text(text=schedule_text(Day.weekType, Day.weekDay))
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_next_day(dp: Dispatcher):
    dp.register_callback_query_handler(next_day, text=["next_day"])


async def change_week(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    Day.weekType = 1 if Day.weekType == 0 else 0
    await call.message.edit_text(text=schedule_text(Day.weekType, Day.weekDay))
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_change_week(dp: Dispatcher):
    dp.register_callback_query_handler(change_week, text=["change_week"])
