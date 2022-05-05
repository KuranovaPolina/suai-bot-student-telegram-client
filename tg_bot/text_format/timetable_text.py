from tg_bot.test_data.test_timetable_data import test_timetable_data

days_name = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}

week_name = {
    1: ("нечётная", "верхняя", "красная"),
    2: ("чётная", "нижняя", "синяя")
}

types_name = {
    1: "Лекция",
    2: "Практическое",
    3: "Лабораторное",
    4: "Коллоквиум",
    5: "Элективное"
}


def format_timetable_text(week_type, week_day):
    lessons_finded = False

    result = f"<b>Расписание на:</b>\n" \
             f"<i>{days_name[week_day]}, " \
             f"{week_name[week_type][0]} - " \
             f"{week_name[week_type][1]} - " \
             f"{week_name[week_type][2]} неделя</i>"

    for lesson in test_timetable_data["lessons"]:
        if lesson["weekDay"] == week_day and lesson["weekType"] == week_type:
            lessons_finded = True
            result += f'\n<b>Группа:</b> {lesson["group"]}\n' \
                      f'<b>Преподаватель:</b> {lesson["teacher"]}\n' \
                      f'<b>Аудитория:</b> {lesson["classRoom"]}\n' \
                      f'<b>Здание:</b> {lesson["building"]}\n' \
                      f'<b>Предмет:</b> {lesson["lessonName"]}\n' \
                      f'<b>Время начала:</b> {lesson["startTime"]}\n' \
                      f'<b>Время окончания:</b> {lesson["endTime"]}\n' \
                      f'<b>Номер пары:</b> {lesson["orderNumber"]}\n' \
                      f'<b>Тип занятия:</b> {types_name[lesson["lessonType"]]}\n'

    if not lessons_finded:
        result += f'\nВыходной'

    return result
