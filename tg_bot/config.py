from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    db_conn_string: str


def load_config(path: str = None):
    env = Env()

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
        ),
        db_conn_string=f'mongodb://{env.str("DB_USER")}:{env.str("DB_PASS")}@{env.str("DB_HOST")}/'
    )
