from aiogram import Dispatcher
from aiogram.types import Message
from tg_bot.keyboards.inline import days_scroll


async def schedule_schedule(message: Message):
    await message.answer(text="Some info", reply_markup=days_scroll)


def register_schedule(dp: Dispatcher):
    dp.register_message_handler(schedule_schedule, commands=["schedule"], state="*")
