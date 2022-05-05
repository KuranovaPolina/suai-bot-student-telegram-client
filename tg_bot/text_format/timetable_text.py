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
    1: ("нечётная", "⬆️", "🔴"),
    2: ("чётная", "⬇️", "🔵")
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
             f"{week_name[week_type][2]}" \
             f"{week_name[week_type][1]} " \
             f"{week_name[week_type][0]} неделя</i>\n"

    for lesson in test_timetable_data["lessons"]:
        if lesson["weekDay"] == week_day and lesson["weekType"] == week_type:
            lessons_finded = True
            result += f'\n<b>{lesson["orderNumber"]}.</b> {lesson["startTime"]} - {lesson["endTime"]}\n' \
                      f'<b>Предмет:</b> {lesson["lessonName"]}, {types_name[lesson["lessonType"]]}\n' \
                      f'<b>Преподаватель:</b> {lesson["teacher"]}\n' \
                      f'<b>Аудитория:</b> {lesson["classRoom"]}\n' \
                      f'<b>Корпус:</b> {lesson["building"]}\n' \
                      f'<b>Группы:</b> {lesson["group"]}\n'

    if not lessons_finded:
        result += f'\nВыходной'

    return result
