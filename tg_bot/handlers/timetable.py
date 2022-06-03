import logging

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

import timetable_message_state_dto
from timetable_message_states_mongo_client import TimetableMessageStatesMongoClient
from tg_bot.keyboards.inline import days_scroll
from tg_bot.text_format.timetable_text import format_timetable_text, find_all_lessons
from tg_bot.dialog_states.timetable_states import TimetableDialog
from tg_bot.users import Day, User, users


class TimetableService:
    def __init__(self, db_client: TimetableMessageStatesMongoClient):
        self.db = db_client

    async def display_timetable(self, message: Message, state: FSMContext):
        user = message.from_user.id
        group = message.text

        actual_week, all_lessons = find_all_lessons(group)

        #
        # await state.reset_state(with_data=False)

        day = Day(actual_week)
        db_state = timetable_message_state_dto.TimetableMessageStateDto(
            dialog_id=message.chat.id,
            day=day.week_day,
            week_type=day.week_type,
            user_id=user,
            timestamp=message.date.timestamp(),
            message_id=message.message_id,
            group=group
        )

        await state.finish()

        if user not in users:
            users[user] = User(user_day=day,
                               user_group_number=group,
                               user_lessons=all_lessons)
        else:
            users[user].user_group_number = day
            users[user].user_group_number = group
            users[user].user_lessons = all_lessons

        msg = await message.answer(text=format_timetable_text(db_state.week_type, db_state.day,
                                                              users[db_state.user_id].user_lessons),
                                   reply_markup=days_scroll,
                                   parse_mode="HTML")

        # msg = await message.answer(text=db_state.group,
        #                            reply_markup=days_scroll,
        #                            parse_mode="HTML")

        db_state.message_id = msg.message_id
        self.db.add_state(db_state)

    async def request_group_number(self, message: Message):
        await message.answer(text="Введите номер группы",
                             parse_mode="HTML")

        await TimetableDialog.group_number.set()

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
            state.week_type = 'нижняя' if state.week_type == 'верхняя' else 'верхняя'
            state.day = 7
        else:
            state.day -= 1

        edited_msg = await call.message.edit_text(text=format_timetable_text(state.week_type, state.day,
                                                                             users[state.user_id].user_lessons),
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
            state.week_type = 'нижняя' if state.week_type == 'верхняя' else 'верхняя'
            state.day = 1
        else:
            state.day += 1

        edited_msg = await call.message.edit_text(text=format_timetable_text(state.week_type, state.day,
                                                                             users[state.user_id].user_lessons),
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

        state.week_type = 'нижняя' if state.week_type == 'верхняя' else 'верхняя'
        edited_msg = await call.message.edit_text(text=format_timetable_text(state.week_type, state.day,
                                                                             users[state.user_id].user_lessons),
                                                  parse_mode="HTML")
        await call.message.edit_reply_markup(reply_markup=days_scroll)

        state.timestamp = edited_msg.edit_date.timestamp()
        self.db.add_state(state)
