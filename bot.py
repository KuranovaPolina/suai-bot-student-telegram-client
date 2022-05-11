import asyncio
import logging

from aiogram import Bot, Dispatcher

from tg_bot.config import load_config
from tg_bot.handlers.timetable import register_full_timetable
from tg_bot.handlers.teacher_info import register_full_teacher_info


logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    register_full_timetable(dp)
    register_full_teacher_info(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(bot)
    bot['config'] = config

    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
