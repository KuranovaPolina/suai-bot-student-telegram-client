from tg_bot.test_schedule_data import test_schedule_data

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


def schedule_text(week_type, week_day):
    lessons_finded = False
    result = f"<b>Расписание на:</b>\n" \
             f"<i>{days_name[week_day]}, " \
             f"{week_name[week_type][0]} - " \
             f"{week_name[week_type][1]} - " \
             f"{week_name[week_type][2]} неделя</i>"
    for i in test_schedule_data["lessons"]:
        if i["weekDay"] == week_day and i["weekType"] == week_type:
            lessons_finded = True
            result += f'\n<b>Группа:</b> {i["group"]}\n' \
                      f'<b>Преподаватель:</b> {i["teacher"]}\n' \
                      f'<b>Аудитория:</b> {i["classRoom"]}\n' \
                      f'<b>Здание:</b> {i["building"]}\n' \
                      f'<b>Предмет:</b> {i["lessonName"]}\n' \
                      f'<b>Время начала:</b> {i["startTime"]}\n' \
                      f'<b>Время окончания:</b> {i["endTime"]}\n' \
                      f'<b>Номер пары:</b> {i["orderNumber"]}\n' \
                      f'<b>Тип занятия:</b> {types_name[i["lessonType"]]}\n'
                      # f'День недели: {i["weekDay"]}\n' \
                      # f'Тип недели: {i["weekType"]}\n'

    if not lessons_finded:
        result += f'\nВыходной'

    return result
