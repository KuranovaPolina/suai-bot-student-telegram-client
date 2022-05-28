from datetime import datetime
from tg_bot.test_data.test_timetable_data import test_timetable_data


class Day:
    def __init__(self, week_type: int = test_timetable_data["actualWeekType"],
                 week_day: int = datetime.isoweekday(datetime.today())):
        self.week_type: int = week_type
        self.week_day: int = week_day


class User:
    def __init__(self, user_day: Day = Day(), user_questions: list = []):
        self.user_day: Day = user_day
        self.user_questions: list = user_questions


users = {}

