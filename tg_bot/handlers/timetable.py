import logging
import time

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

import TimetableMessageStateDto
from TimetableMessageStatesMongoClient import TimetableMessageStatesMongoClient
from tg_bot.keyboards.inline import days_scroll
from tg_bot.text_format.timetable_text import format_timetable_text
from tg_bot.users import users, User, Day

# Пробросить через DI
client = TimetableMessageStatesMongoClient('mongodb://localhost:27017')


async def display_timetable(message: Message):
    user = message.from_user.id

    day = Day()
    state = TimetableMessageStateDto.TimetableMessageStateDto(
        dialog_id=message.chat.id,
        day=day.week_day,
        week_type=day.week_type,
        user_id=user,
        timestamp=message.date.timestamp(),
        message_id=message.message_id,
        group='test'
    )

    msg = await message.answer(text=format_timetable_text(state.week_type,
                                                          state.day),
                               reply_markup=days_scroll,
                               parse_mode="HTML")
    state.message_id = msg.message_id
    client.add_state(state)
    print(msg.message_id)


def register_timetable(dp: Dispatcher):
    dp.register_message_handler(display_timetable,
                                commands=["timetable"],
                                state="*")


async def scroll_previous_day(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    state = client.get_state(dialog_id=call.message.chat.id, message_id=call.message.message_id)

    if not state:
        logging.warning(f"State not exist")
        logging.info(f"{callback_data=}")
        logging.info(f"{call.message}")
        logging.info(f"{call.message.from_user.id}")
        await call.message.edit_text(text='Ошибка, запросите новое расписание!',
                                     parse_mode="HTML")
        return

    logging.info(f"{callback_data=}")

    if state.day == 1:
        state.week_type = 2 if state.week_type == 1 else 1
        state.day = 7
    else:
        state.day -= 1

    edited_msg = await call.message.edit_text(text=format_timetable_text(state.week_type, state.day),
                                              parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=days_scroll)

    state.timestamp = edited_msg.edit_date.timestamp()
    client.add_state(state)


def register_previous_day(dp: Dispatcher):
    dp.register_callback_query_handler(scroll_previous_day,
                                       text=["scroll_previous_day"])


async def scroll_next_day(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    state = client.get_state(dialog_id=call.message.chat.id, message_id=call.message.message_id)

    if not state:
        logging.warning(f"State not exist")
        logging.info(f"{callback_data=}")
        logging.info(f"{call.message}")
        logging.info(f"{call.message.from_user.id}")
        await call.message.edit_text(text='Ошибка, запросите новое расписание!',
                                     parse_mode="HTML")
        return

    logging.info(f"{callback_data=}")

    if state.day == 7:
        state.week_type = 2 if state.week_type == 1 else 1
        state.day = 1
    else:
        state.day += 1

    edited_msg = await call.message.edit_text(text=format_timetable_text(state.week_type, state.day),
                                              parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=days_scroll)

    state.timestamp = edited_msg.edit_date.timestamp()
    client.add_state(state)


def register_next_day(dp: Dispatcher):
    dp.register_callback_query_handler(scroll_next_day,
                                       text=["scroll_next_day"])


async def change_week(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    state = client.get_state(dialog_id=call.message.chat.id, message_id=call.message.message_id)

    if not state:
        logging.warning(f"State not exist")
        logging.info(f"{callback_data=}")
        logging.info(f"{call.message}")
        logging.info(f"{call.message.from_user.id}")
        await call.message.edit_text(text='Ошибка, запросите новое расписание!',
                                     parse_mode="HTML")
        return

    logging.info(f"{callback_data=}")

    state.week_type = 2 if state.week_type == 1 else 1
    edited_msg = await call.message.edit_text(text=format_timetable_text(state.week_type, state.day),
                                              parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=days_scroll)

    state.timestamp = edited_msg.edit_date.timestamp()
    client.add_state(state)


def register_change_week(dp: Dispatcher):
    dp.register_callback_query_handler(change_week,
                                       text=["change_week"])


def register_full_timetable(dp: Dispatcher):
    register_timetable(dp)
    register_previous_day(dp)
    register_next_day(dp)
    register_change_week(dp)
