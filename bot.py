import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tg_bot.config import load_config

from service_handlers_registrars.teacher_info_service_handlers_registrar import TeacherInfoServiceHandlersRegistrar
from tg_bot.handlers.teacher_info import TeacherInfoService

from TimetableMessageStatesMongoClient import TimetableMessageStatesMongoClient
from TimetableServiceHandlersRegistrator import TimetableServiceHandlersRegistrator
from tg_bot.handlers.timetable import TimetableService


logger = logging.getLogger(__name__)


def register_all_handlers(dp: Dispatcher, registrars: list):
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


    timetable_db_client = TimetableMessageStatesMongoClient(config.db_conn_string)
    timetable_service = TimetableService(timetable_db_client)
    timetable_service_registrator = TimetableServiceHandlersRegistrator(timetable_service)
    
    teacher_info_service = TeacherInfoService()
    teacher_info_service_registrar = TeacherInfoServiceHandlersRegistrar(teacher_info_service)
    
    register_all_handlers(dp, [timetable_service_registrator,
                              teacher_info_service_registrar])
    
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
