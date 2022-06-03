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

    def format_teacher_info_text(self) -> str:
        result: str = f'\n<i>{self.name}.</i>\n' \
                      f'<b>Академическая степень</b> {self.academic_degree}\n' \
                      f'<b>Должность</b> {self.position}\n' \
                      f'<b>Факультет</b> {self.institute}\n' \
                      f'<b>Кафедра</b> {self.department}\n'

        if self.phone != "":
            result += f'<b>Номер</b> {self.phone}\n'

        if self.email != "":
            result += f'<b>Почта</b> {self.email}\n'

        return result


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
