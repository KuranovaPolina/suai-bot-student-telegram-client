import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from TeacherInfoServiceHandlersRegistrar import TeacherInfoServiceHandlersRegistrar
from tg_bot.config import load_config
from tg_bot.handlers.timetable import register_full_timetable
from tg_bot.handlers.teacher_info import TeacherInfo


logger = logging.getLogger(__name__)


def register_all_handlers(dp, registrars: list):
    register_full_timetable(dp)

    for registrar in registrars:
        registrar.register_all(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=MemoryStorage())
    bot['config'] = config

    teacher_info_service = TeacherInfo()
    teacher_info_service_registrar = TeacherInfoServiceHandlersRegistrar(teacher_info_service)
    register_all_handlers(dp, [teacher_info_service_registrar])

    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
