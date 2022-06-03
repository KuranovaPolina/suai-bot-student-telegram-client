from datetime import datetime


class Day:
    def __init__(self, week_type: str = "верхняя",
                 week_day: int = datetime.isoweekday(datetime.today())):
        self.week_type: str = week_type
        self.week_day: int = week_day


class User:
    def __init__(self, user_day: Day = Day(),
                 teacher_name: str = "", teachers: list = None,
                 teacher_number: int = 0,
                 user_questions: list = None,
                 user_group_number: int = 0,
                 user_lessons: list = None):

        if teachers is None:
            teachers = []
        if user_lessons is None:
            user_lessons = []
        if user_questions is None:
            user_questions = []

        self.user_day: Day = user_day
        self.teacher_name: str = teacher_name
        self.teachers: list = teachers
        self.teacher_number = teacher_number
        self.user_questions: list = user_questions
        self.user_group_number: int = user_group_number
        self.user_lessons = user_lessons


users = {}

