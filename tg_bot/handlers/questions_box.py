import logging

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from tg_bot.dialog_states.questions_box_states import QuestionsBoxDialog
from tg_bot.users import User, users


async def save_questions(message: Message, state: FSMContext):
    answer = message.text
    user = message.from_user.id

    if user not in users:
        users[user] = User(user_questions=[answer])

    else:
        users[user].user_questions.append(answer)

    await state.finish()

    await message.answer(text=f"Answer saved {users[user].user_questions}",
                         parse_mode="HTML")


def register_save_questions(dp: Dispatcher):
    dp.register_message_handler(save_questions,
                                state=QuestionsBoxDialog.question)


async def request_question(message: Message):
    await message.answer(text="Задайте вопрос", parse_mode="HTML")

    await QuestionsBoxDialog.question.set()


def register_request_question(dp: Dispatcher):
    dp.register_message_handler(request_question,
                                commands=["ask_question"],
                                state="*")


def register_full_questions_box(dp: Dispatcher):
    register_save_questions(dp)
    register_request_question(dp)
