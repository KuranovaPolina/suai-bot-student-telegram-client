import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from tg_bot.keyboards.inline import days_scroll


async def schedule_schedule(message: Message):
    await message.answer(text="Start info",
                         reply_markup=days_scroll)


def register_schedule(dp: Dispatcher):
    dp.register_message_handler(schedule_schedule,
                                commands=["schedule"],
                                state="*")


async def previous_day(call: CallbackQuery):
    await call.answer(cache_time=10)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    await call.message.edit_text(text="Previous day info")
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_pr_day(dp: Dispatcher):
    dp.register_callback_query_handler(previous_day, text=["pr_day"])


async def next_day(call: CallbackQuery):
    await call.answer(cache_time=10)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    await call.message.edit_text(text="Next day info")
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_next_day(dp: Dispatcher):
    dp.register_callback_query_handler(next_day, text=["next_day"])


async def change_week(call: CallbackQuery):
    await call.answer(cache_time=10)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    await call.message.edit_text(text="Another week info")
    await call.message.edit_reply_markup(reply_markup=days_scroll)


def register_change_week(dp: Dispatcher):
    dp.register_callback_query_handler(change_week, text=["change_week"])
