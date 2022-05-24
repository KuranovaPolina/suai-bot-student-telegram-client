from aiogram import Dispatcher

from tg_bot.handlers.teacher_info import TeacherInfo
from tg_bot.dialog_states.teacher_info_search_state import TeacherDialog


class TeacherInfoServiceHandlersRegistrar:
    def __init__(self, teacher_info_service: TeacherInfo):
        self.service = teacher_info_service

    def register_display_teachers(self, dp: Dispatcher):
        dp.register_message_handler(self.service.display_teachers,
                                    state=TeacherDialog.answer)

    def register_request_teacher_name(self, dp: Dispatcher):
        dp.register_message_handler(self.service.request_teacher_name,
                                    commands=["teacher_info"],
                                    state="*")

    def register_previous_teacher_info(self, dp: Dispatcher):
        dp.register_callback_query_handler(self.service.scroll_previous_teacher_info,
                                           text=["scroll_previous_teacher_info"])

    def register_next_teacher_info(self, dp: Dispatcher):
        dp.register_callback_query_handler(self.service.scroll_next_teacher_info,
                                           text=["scroll_next_teacher_info"])

    def register_all(self, dp: Dispatcher):
        self.register_display_teachers(dp)
        self.register_request_teacher_name(dp)
        self.register_previous_teacher_info(dp)
        self.register_next_teacher_info(dp)
