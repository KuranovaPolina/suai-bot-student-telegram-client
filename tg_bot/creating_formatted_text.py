from tg_bot.test_schedule_data import test_schedule_data

days_name = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье"
}

week_name = {
    0: ("чётная", "нижняя", "синяя"),
    1: ("нечётная", "верхняя", "красная")
}


def schedule_text(week_type, week_day):
    lessons_finded = False
    result = f"Расписание на:\n" \
             f"{days_name[week_day]}, " \
             f"{week_name[week_type][0]} - {week_name[week_type][1]} - {week_name[week_type][2]} неделя"
    for i in test_schedule_data["lessons"]:
        if i["weekDay"] == week_day and i["weekType"] == week_type:
            lessons_finded = True
            result += f'\nГруппа: {i["group"]}\n' \
                      f'Преподаватель: {i["teacher"]}\n' \
                      f'Аудитория: {i["classRoom"]}\n' \
                      f'Здание: {i["building"]}\n' \
                      f'Предмет: {i["lessonName"]}\n' \
                      f'Время начала: {i["startTime"]}\n' \
                      f'Время окончания: {i["endTime"]}\n' \
                      f'Номер пары: {i["order"]}\n'
                      # f'День недели: {i["weekDay"]}\n' \
                      # f'Тип недели: {i["weekType"]}\n'

    if not lessons_finded:
        result += f'\nВыходной'

    return result
