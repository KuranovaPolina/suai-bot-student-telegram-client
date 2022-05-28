import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from TimetableMessageStatesMongoClient import TimetableMessageStatesMongoClient
from TimetableServiceHandlersRegistrator import TimetableServiceHandlersRegistrator
from service_handlers_registrars.questions_box_service_handlers_registrar import QuestionsBoxServiceHandlersRegistrar
from tg_bot.config import load_config
from tg_bot.handlers.timetable import TimetableService
from tg_bot.handlers.questions_box import QuestionsBoxService


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
    timetable_service_registrar = TimetableServiceHandlersRegistrator(timetable_service)

    questions_box_service = QuestionsBoxService()
    questions_box_service_registrar = QuestionsBoxServiceHandlersRegistrar(questions_box_service)

    register_all_handlers(dp, [timetable_service_registrar,
                               questions_box_service_registrar])

    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
