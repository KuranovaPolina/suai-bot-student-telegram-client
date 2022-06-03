from aiogram.types import Message
from tg_bot.keyboards.reply import greet_kb


async def start(message: Message):
    await message.answer(text="Привет", reply_markup=greet_kb, parse_mode="HTML")



