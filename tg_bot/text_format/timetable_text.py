from official_data.official_timetable_data import get_official_teacher_info_data

days_name = {
    0: "Вне сетки расписания",
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}

days_number = {
    "Вне сетки расписания": 0,
    "Понедельник": 1,
    "Вторник": 2,
    "Среда": 3,
    "Четверг": 4,
    "Пятница": 5,
    "Суббота": 6,
    "Воскресенье": 7
}

week_name = {
    "верхняя": ("нечётная", "⬆️", "🔴"),
    "нижняя": ("чётная", "⬇️", "🔵")
}

types_name = {
    1: "Лекция",
    2: "Практическое",
    3: "Лабораторное",
    4: "Коллоквиум",
    5: "Элективное"
}


class Lesson:
    def __init__(self, groups: list, teachers: list,
                 building: str, class_rooms: list,
                 week_day: int, week_types: list,
                 lesson_type: str, name: str,
                 start_time: str, end_time: str,
                 order: str):
        self.groups: list = groups
        self.teachers: list = teachers
        self.building: str = building
        self.class_rooms: list = class_rooms
        self.week_day: int = week_day
        self.week_types: list = week_types
        self.lesson_type: str = lesson_type
        self.name: str = name
        self.start_time: str = start_time
        self.end_time: str = end_time
        self.order: str = order


def connect_all_elements(list_elements) -> str:
    result: str = ""

    for element in list_elements:
        result += '\n\t' + element

    return result


def format_timetable_text(week_type: str, week_day: int, lessons: list) -> str:
    day_lessons = find_all_day_lessons(week_type, week_day, lessons)

    result: str = f"<b>Расписание на:</b>\n" \
                  f"<i>{days_name[week_day]}, " \
                  f"{week_name[week_type][2]}" \
                  f"{week_name[week_type][1]} " \
                  f"{week_name[week_type][0]} неделя</i>\n"

    if not day_lessons:
        result += f'\nВыходной'

    for lesson in day_lessons:
        result += f'\n<b>{lesson.order}.</b> {lesson.start_time} - {lesson.end_time}\n' \
                  f'<b>Предмет:</b> {lesson.name}, {lesson.lesson_type}\n' \
                  f'<b>Преподаватели:</b> {connect_all_elements(lesson.teachers)}\n' \
                  f'<b>Аудитории:</b> {connect_all_elements(lesson.class_rooms)}\n' \
                  f'<b>Корпус:</b> {lesson.building}\n' \
                  f'<b>Группы:</b> {connect_all_elements(lesson.groups)}\n'

    return result


def create_elements_list(lesson: dict, key: str) -> list:
    elements = []
    for element in lesson[key]:
        if element != "":
            elements.append(element)

    return elements


def find_all_lessons(key_string: str) -> tuple:
    lessons = []

    data = get_official_teacher_info_data(key_string)

    for lesson in data["Lessons"]:
        lessons.append(Lesson(create_elements_list(lesson, "Groups"), create_elements_list(lesson, "Teachers"),
                              lesson["Building"], create_elements_list(lesson, "ClassRooms"),
                              days_number[lesson["WeekDay"]], create_elements_list(lesson, "WeekTypes"),
                              lesson["Type"], lesson["Name"],
                              lesson["StartTime"], lesson["EndTime"],
                              lesson["OrderNumber"]))

    return data["ActualWeekType"], lessons


def find_all_day_lessons(week_type: str, week_day: int, lessons: list) -> list:
    day_lessons = []

    for lesson in lessons:
        if week_type in lesson.week_types and (week_day == lesson.week_day):
            day_lessons.append(lesson)

    return day_lessons
