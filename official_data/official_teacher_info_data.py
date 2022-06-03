import requests


def get_official_teacher_info_data(last_name: str = "Аграновский") -> dict:

    request_result = requests.get("https://suai.callmemars1.software/teacherInfo.get?lastName=" + last_name)

    return request_result.json()

    # return {
    #     "Teachers": [
    #         {
    #             "FirstName": "Andrey",
    #             "SecondName": "Vladimirovich",
    #             "LastName": "Agranovskiy",
    #             "Positions": [
    #                 {
    #                     "Institute": "inst1",
    #                     "Department": "dep1",
    #                     "Position": "docent"
    #                 },
    #                 {
    #                     "Institute": "inst2",
    #                     "Department": "dep2",
    #                     "Position": "docent"
    #                 }
    #             ],
    #             "Phone": "",
    #             "Email": "a_agranovskii@mail.ru",
    #             "TeacherDegree": "docent",
    #             "ClassRoom": "52-13",
    #             "AcademicDegrees": [
    #                 "KaMAAT",
    #                 "KaMAAT"
    #             ]
    #         },
    #         {
    #             "FirstName": "Valeriy",
    #             "SecondName": "anatolxfhmx",
    #             "LastName": "dfhjs",
    #             "Positions": [
    #                 {
    #                     "Institute": "inst3",
    #                     "Department": "dep3",
    #                     "Position": "docent"
    #                 },
    #                 {
    #                     "Institute": "inst4",
    #                     "Department": "dep4",
    #                     "Position": "docent"
    #                 }
    #             ],
    #             "Phone": "",
    #             "Email": "a_agranovskii@mail.ru",
    #             "TeacherDegree": "docent",
    #             "ClassRoom": "52-13",
    #             "AcademicDegrees": [
    #                 "KaMAAT",
    #                 "KaMAAT"
    #             ]
    #         }
    #     ]
    # }


# print(get_official_teacher_info_data())
