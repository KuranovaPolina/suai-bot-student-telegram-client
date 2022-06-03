from aiogram import Dispatcher

from tg_bot.handlers.start import start


def register_start(dp: Dispatcher):
    dp.register_message_handler(start,
                                commands=["start"],
                                state="*")
