import requests


def get_official_timetable_data(group: str = "5038") -> dict:

    request_result = requests.get("https://suai.callmemars1.software/timetable.get?group=" + group)

    return request_result.json()


# print(get_official_teacher_info_data())
