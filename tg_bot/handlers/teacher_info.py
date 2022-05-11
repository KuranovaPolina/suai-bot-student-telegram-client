import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from tg_bot.keyboards.inline import teacher_scroll
# from tg_bot.text_format.teacher_info_text import
# from tg_bot.users import users, User, Day


async def display_teachers(message: Message):
    user = message.from_user.id

    await message.answer(text="Some teacher info",
                         reply_markup=teacher_scroll,
                         parse_mode="HTML")


def register_teacher_info(dp: Dispatcher):
    dp.register_message_handler(display_teachers,
                                commands=["teacher_info"],
                                state="*")


async def scroll_previous_teacher_info(call: CallbackQuery):
    await call.answer(cache_time=1)
    user = call.from_user.id

    callback_data = call.data

    logging.info(f"{callback_data=}")

    await call.message.edit_text(text="Some previous teacher info",
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

    await call.message.edit_text(text="Some next teacher info",
                                 parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=teacher_scroll)


def register_next_teacher_info(dp: Dispatcher):
    dp.register_callback_query_handler(scroll_next_teacher_info,
                                       text=["scroll_next_teacher_info"])


def register_full_teacher_info(dp: Dispatcher):
    register_teacher_info(dp)
    register_previous_teacher_info(dp)
    register_next_teacher_info(dp)
