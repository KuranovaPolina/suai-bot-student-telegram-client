import requests


def get_official_teacher_info_data(group: str = "5038") -> dict:

    request_result = requests.get("https://suai.callmemars1.software/timetable.get?group=" + group)

    # return request_result.json()

    return {
        "ActualWeekType": "нижняя",
          "Lessons": [
            {
              "Groups": [
                "5011",
                "5012",
                "5013",
                "5021",
                "5022",
                "5023",
                "5031",
                "5036",
                "5037",
                "5038"
              ],
              "Teachers": [
                "Борисенок А.А. - старший преподаватель"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "спортзал*"
              ],
              "WeekDay": "Среда",
              "WeekTypes": [
                "верхняя",
                "нижняя"
              ],
              "Type": "ПР",
              "Name": "Прикладная физическая культура (элективный модуль)",
              "StartTime": "16:40",
              "EndTime": "18:10",
              "OrderNumber": "5"
            },
            {
              "Groups": [
                "5011",
                "5012",
                "5013",
                "5021",
                "5022",
                "5023",
                "5031",
                "5036",
                "5037",
                "5038"
              ],
              "Teachers": [
                "Борисенок А.А. - старший преподаватель"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "спортзал*"
              ],
              "WeekDay": "Суббота",
              "WeekTypes": [
                "верхняя",
                "нижняя"
              ],
              "Type": "ПР",
              "Name": "Прикладная физическая культура (элективный модуль)",
              "StartTime": "13:00",
              "EndTime": "14:30",
              "OrderNumber": "3"
            },
            {
              "Groups": [
                "5031",
                "5036",
                "5037",
                "5038"
              ],
              "Teachers": [
                "Дьякова Г.Н. - доцент, канд. физ.-мат. наук, доцент"
              ],
              "Building": "Гастелло 15",
              "ClassRooms": [
                "32-02"
              ],
              "WeekDay": "Понедельник",
              "WeekTypes": [
                "верхняя",
                "нижняя"
              ],
              "Type": "Л",
              "Name": "Вычислительная математика",
              "StartTime": "9:30",
              "EndTime": "11:00",
              "OrderNumber": "1"
            },
            {
              "Groups": [
                "5031",
                "5036",
                "5037",
                "5038"
              ],
              "Teachers": [
                "Плотникова В.А. - старший преподаватель"
              ],
              "Building": "Гастелло 15",
              "ClassRooms": [
                "32-02"
              ],
              "WeekDay": "Понедельник",
              "WeekTypes": [
                "верхняя"
              ],
              "Type": "Л",
              "Name": "Социология",
              "StartTime": "11:10",
              "EndTime": "12:40",
              "OrderNumber": "2"
            },
            {
              "Groups": [
                "5031",
                "5036",
                "5037",
                "5038"
              ],
              "Teachers": [
                "Калюжный В.П. - доцент, канд. техн. наук, доцент"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "52-35"
              ],
              "WeekDay": "Вторник",
              "WeekTypes": [
                "нижняя"
              ],
              "Type": "Л",
              "Name": "Инструментальные средства информационных систем",
              "StartTime": "15:00",
              "EndTime": "16:30",
              "OrderNumber": "4"
            },
            {
              "Groups": [
                "5031",
                "5036",
                "5037",
                "5038"
              ],
              "Teachers": [
                "Семененко Т.В. - старший преподаватель"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "52-43"
              ],
              "WeekDay": "Среда",
              "WeekTypes": [
                "нижняя"
              ],
              "Type": "Л",
              "Name": "Управление данными",
              "StartTime": "15:00",
              "EndTime": "16:30",
              "OrderNumber": "4"
            },
            {
              "Groups": [
                "5031",
                "5036",
                "5037",
                "5038"
              ],
              "Teachers": [
                "Семененко Т.В. - старший преподаватель"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "52-43"
              ],
              "WeekDay": "Среда",
              "WeekTypes": [
                "нижняя"
              ],
              "Type": "Л",
              "Name": "Управление данными",
              "StartTime": "18:30",
              "EndTime": "20:00",
              "OrderNumber": "6"
            },
            {
              "Groups": [
                "5031",
                "5036",
                "5037",
                "5038"
              ],
              "Teachers": [
                "Суетина Т.А. - старший преподаватель"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "52-18"
              ],
              "WeekDay": "Пятница",
              "WeekTypes": [
                "верхняя",
                "нижняя"
              ],
              "Type": "Л",
              "Name": "Технологии программирования",
              "StartTime": "9:30",
              "EndTime": "11:00",
              "OrderNumber": "1"
            },
            {
              "Groups": [
                "5031",
                "5036",
                "5037",
                "5038"
              ],
              "Teachers": [
                "Аграновский А.В. - доцент, канд. техн. наук, доцент"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "52-35"
              ],
              "WeekDay": "Пятница",
              "WeekTypes": [
                "верхняя",
                "нижняя"
              ],
              "Type": "Л",
              "Name": "Компьютерная графика",
              "StartTime": "13:00",
              "EndTime": "14:30",
              "OrderNumber": "3"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                ""
              ],
              "Building": "",
              "ClassRooms": [
                "на базе кафедры КАФЕДРА 53"
              ],
              "WeekDay": "Вне сетки расписания",
              "WeekTypes": [
                "верхняя",
                "нижняя"
              ],
              "Type": "КР",
              "Name": "Технологии программирования",
              "StartTime": "",
              "EndTime": "",
              "OrderNumber": "Вне сетки расписания"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Дьякова Г.Н. - доцент, канд. физ.-мат. наук, доцент"
              ],
              "Building": "Гастелло 15",
              "ClassRooms": [
                "22-06"
              ],
              "WeekDay": "Понедельник",
              "WeekTypes": [
                "нижняя"
              ],
              "Type": "ПР",
              "Name": "Вычислительная математика",
              "StartTime": "11:10",
              "EndTime": "12:40",
              "OrderNumber": "2"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Карпова О.П. - старший преподаватель"
              ],
              "Building": "Гастелло 15",
              "ClassRooms": [
                "34-04"
              ],
              "WeekDay": "Понедельник",
              "WeekTypes": [
                "верхняя",
                "нижняя"
              ],
              "Type": "ПР",
              "Name": "Иностранный язык",
              "StartTime": "13:00",
              "EndTime": "14:30",
              "OrderNumber": "3"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Плотникова В.А. - старший преподаватель"
              ],
              "Building": "Гастелло 15",
              "ClassRooms": [
                "12-04"
              ],
              "WeekDay": "Понедельник",
              "WeekTypes": [
                "верхняя"
              ],
              "Type": "ПР",
              "Name": "Социология",
              "StartTime": "15:00",
              "EndTime": "16:30",
              "OrderNumber": "4"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Красильникова О.И. - доцент, канд. техн. наук, доцент"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "23-17"
              ],
              "WeekDay": "Вторник",
              "WeekTypes": [
                "верхняя"
              ],
              "Type": "ЛР",
              "Name": "Основы информационных технологий в медиаиндустрии",
              "StartTime": "18:30",
              "EndTime": "20:00",
              "OrderNumber": "6"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Красильникова О.И. - доцент, канд. техн. наук, доцент"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "23-17"
              ],
              "WeekDay": "Вторник",
              "WeekTypes": [
                "нижняя"
              ],
              "Type": "Л",
              "Name": "Основы информационных технологий в медиаиндустрии",
              "StartTime": "18:30",
              "EndTime": "20:00",
              "OrderNumber": "6"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Красильникова О.И. - доцент, канд. техн. наук, доцент"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "33-04"
              ],
              "WeekDay": "Среда",
              "WeekTypes": [
                "верхняя"
              ],
              "Type": "ЛР",
              "Name": "Основы информационных технологий в медиаиндустрии",
              "StartTime": "13:00",
              "EndTime": "14:30",
              "OrderNumber": "3"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Ушаков В.А. - старший преподаватель"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "33-05"
              ],
              "WeekDay": "Суббота",
              "WeekTypes": [
                "нижняя"
              ],
              "Type": "ЛР",
              "Name": "Компьютерная графика",
              "StartTime": "9:30",
              "EndTime": "11:00",
              "OrderNumber": "1"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Кучерук Т.В. - ассистент"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "33-04"
              ],
              "WeekDay": "Суббота",
              "WeekTypes": [
                "верхняя",
                "нижняя"
              ],
              "Type": "ЛР",
              "Name": "Управление данными",
              "StartTime": "11:10",
              "EndTime": "12:40",
              "OrderNumber": "2"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Ушаков В.А. - старший преподаватель"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "33-02"
              ],
              "WeekDay": "Суббота",
              "WeekTypes": [
                "верхняя",
                "нижняя"
              ],
              "Type": "ЛР",
              "Name": "Инструментальные средства информационных систем",
              "StartTime": "15:00",
              "EndTime": "16:30",
              "OrderNumber": "4"
            },
            {
              "Groups": [
                "5038"
              ],
              "Teachers": [
                "Агеев М.П. - ассистент"
              ],
              "Building": "Б.Морская 67",
              "ClassRooms": [
                "33-04"
              ],
              "WeekDay": "Суббота",
              "WeekTypes": [
                "верхняя"
              ],
              "Type": "ЛР",
              "Name": "Технологии программирования",
              "StartTime": "16:40",
              "EndTime": "18:10",
              "OrderNumber": "5"
            }
          ]
        }


# print(get_official_teacher_info_data())
