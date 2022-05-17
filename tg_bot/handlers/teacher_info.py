import logging

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from tg_bot.keyboards.inline import teacher_scroll
from tg_bot.states.teacher_info_search_state import TeacherDialog


async def display_teachers(message: Message, state: FSMContext):
    user = message.from_user.id
    answer = message.text

    async with state.proxy() as data:
        data['teacher_name'] = answer
        # teache = data['text']

    await message.answer(text=f"{data['teacher_name']}",
                         reply_markup=teacher_scroll,
                         parse_mode="HTML")

    await state.finish()


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
    register_display_teachers(dp)
    register_ask_teacher(dp)
    register_previous_teacher_info(dp)
    register_next_teacher_info(dp)
