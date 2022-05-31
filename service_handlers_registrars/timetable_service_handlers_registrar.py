from aiogram import Dispatcher

from tg_bot.handlers.timetable import TimetableService


class TimetableServiceHandlersRegistrar:
    def __init__(self, timetable_service: TimetableService):
        self.service = timetable_service

    def register_timetable(self, dp: Dispatcher):
        dp.register_message_handler(self.service.display_timetable,
                                    commands=["timetable"],
                                    state="*")

    def register_previous_day(self, dp: Dispatcher):
        dp.register_callback_query_handler(self.service.scroll_previous_day,
                                           text=["scroll_previous_day"])

    def register_next_day(self, dp: Dispatcher):
        dp.register_callback_query_handler(self.service.scroll_next_day,
                                           text=["scroll_next_day"])

    def register_change_week(self, dp: Dispatcher):
        dp.register_callback_query_handler(self.service.change_week,
                                           text=["change_week"])

    def register_all(self, dp: Dispatcher):
        self.register_timetable(dp)
        self.register_previous_day(dp)
        self.register_next_day(dp)
        self.register_change_week(dp)
