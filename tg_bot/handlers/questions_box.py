import logging

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from tg_bot.dialog_states.questions_box_states import QuestionsBoxDialog
from tg_bot.users import User, users


class QuestionsBoxService:
    def __init__(self):
        pass

    async def save_questions(self, message: Message, state: FSMContext):
        answer = message.text
        user = message.from_user.id

        if user not in users:
            users[user] = User(user_questions=[answer])

        else:
            users[user].user_questions.append(answer)

        await state.finish()

        await message.answer(text=f"Answer saved {users[user].user_questions}",
                             parse_mode="HTML")

    async def request_question(self, message: Message):
        await message.answer(text="Задайте вопрос", parse_mode="HTML")

        await QuestionsBoxDialog.question.set()
