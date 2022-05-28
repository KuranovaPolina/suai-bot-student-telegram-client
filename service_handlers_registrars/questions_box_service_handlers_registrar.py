from aiogram import Dispatcher

from tg_bot.handlers.questions_box import QuestionsBoxService
from tg_bot.dialog_states.questions_box_states import QuestionsBoxDialog


class QuestionsBoxServiceHandlersRegistrar:
    def __init__(self, question_box_service: QuestionsBoxService):
        self.service = question_box_service

    def register_save_questions(self, dp: Dispatcher):
        dp.register_message_handler(self.service.save_questions,
                                    state=QuestionsBoxDialog.question)

    def register_request_question(self, dp: Dispatcher):
        dp.register_message_handler(self.service.request_question,
                                    commands=["ask_question"],
                                    state="*")

    def register_all(self, dp: Dispatcher):
        self.register_save_questions(dp)
        self.register_request_question(dp)
