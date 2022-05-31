import logging

from aiogram.types import Message, CallbackQuery

import timetable_message_state_dto
from timetable_message_states_mongo_client import TimetableMessageStatesMongoClient
from tg_bot.keyboards.inline import days_scroll
from tg_bot.text_format.timetable_text import format_timetable_text
from tg_bot.users import users, User, Day


class TimetableService:
    def __init__(self, db_client: TimetableMessageStatesMongoClient):
        self.db = db_client

    async def display_timetable(self, message: Message):
        user = message.from_user.id

        day = Day()
        state = timetable_message_state_dto.TimetableMessageStateDto(
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
        self.db.add_state(state)

    async def scroll_previous_day(self, call: CallbackQuery):
        await call.answer(cache_time=1)

        callback_data = call.data

        state = self.db.get_state(dialog_id=call.message.chat.id, message_id=call.message.message_id)

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
        self.db.add_state(state)

    async def scroll_next_day(self, call: CallbackQuery):
        await call.answer(cache_time=1)

        callback_data = call.data

        state = self.db.get_state(dialog_id=call.message.chat.id, message_id=call.message.message_id)

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
        self.db.add_state(state)

    async def change_week(self, call: CallbackQuery):
        await call.answer(cache_time=1)

        callback_data = call.data

        state = self.db.get_state(dialog_id=call.message.chat.id, message_id=call.message.message_id)

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
        self.db.add_state(state)
