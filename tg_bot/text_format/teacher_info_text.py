from tg_bot.test_data.test_teacher_info_data import test_teacher_data


class Teacher:
    def __init__(self, name: str,
                 academic_degree: str, position: str,
                 institute: str, department: str,
                 phone: str, email: str):
        self.name: str = name
        self.academic_degree: str = academic_degree
        self.position: str = position
        self.institute: str = institute
        self.department: str = department
        self.phone: str = phone
        self.email: str = email


def find_all_teachers(key_string: str) -> list:
    teachers = []
    for teacher in test_teacher_data["teachers"]:
        if key_string in teacher["name"]:
            teachers.append(Teacher(teacher["name"],
                                    teacher["academicDegree"],
                                    teacher["position"],
                                    teacher["institute"],
                                    teacher["department"],
                                    teacher["phone"],
                                    teacher["email"]))

    return teachers


def format_timetable_text(teacher: Teacher) -> str:
    result: str = f'\n<i>{teacher.name}.</i>\n' \
                  f'<b>Академическая степень</b> {teacher.academic_degree}\n' \
                  f'<b>Должность</b> {teacher.position}\n' \
                  f'<b>Факультет</b> {teacher.institute}\n' \
                  f'<b>Кафедра</b> {teacher.department}\n' \
                  f'<b>Номер</b> {teacher.phone}\n' \
                  f'<b>Почта</b> {teacher.email}\n'

    return result
