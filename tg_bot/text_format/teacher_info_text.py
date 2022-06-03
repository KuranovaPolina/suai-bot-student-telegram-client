from official_data.official_teacher_info_data import get_official_teacher_info_data


class Position:
    def __init__(self, institute: str, department: str, position: str):
        self.institute: str = institute
        self.department: str = department
        self.position: str = position

    def format_position_text(self) -> str:
        return f'\n\t<i>Факультет:</i> {self.institute}\n' \
               f'\t<i>Кафедра:</i> {self.department}\n' \
               f'\t<i>Должность:</i> {self.position}\n'


class Teacher:
    def __init__(self, first_name: str, second_name: str, last_name: str,
                 positions: list,
                 phone: str, email: str,
                 teacher_degree: str, class_room: str,
                 academic_degrees: list):
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.last_name: str = last_name
        self.positions: list = positions  # institute, department, position
        self.phone: str = phone
        self.email: str = email
        self.teacher_degree: str = teacher_degree
        self.class_room: str = class_room
        self.academic_degrees: list = academic_degrees

    def connect_all_positions(self) -> str:
        result: str = ""

        for position in self.positions:
            result += position.format_position_text()

        return result

    def connect_all_academic_degrees(self) -> str:
        result: str = ""

        for academic_degree in self.academic_degrees:
            result += '\n\t' + academic_degree

        return result

    def format_teacher_info_text(self) -> str:

        result: str = f'\n<i>{self.first_name} {self.second_name} {self.last_name}.</i>\n' \
                      f'<b>Должности</b>:{self.connect_all_positions()}\n' \
                      f'<b>Степень преподавателя</b>: {self.teacher_degree}\n' \
                      f'<b>Академические степени</b>:{self.connect_all_academic_degrees()}\n' \
                      f'<b>Аудитория</b>: {self.class_room}\n'

        if self.phone != "":
            result += f'<b>Номер</b>: {self.phone}\n'

        if self.email != "":
            result += f'<b>Почта</b>: {self.email}\n'

        return result


def create_positions(teacher: dict) -> list:
    positions = []
    for position in teacher["Positions"]:
        positions.append(Position(position["Institute"],
                                  position["Department"],
                                  position["Position"]))

    return positions


def create_academic_degrees(teacher: dict) -> list:
    academic_degrees = []
    for academic_degree in teacher["AcademicDegrees"]:
        academic_degrees.append(academic_degree)

    return academic_degrees


def find_all_teachers(key_string: str) -> list:
    teachers = []

    for teacher in get_official_teacher_info_data(key_string)["Teachers"]:

        teachers.append(Teacher(teacher["FirstName"], teacher["SecondName"], teacher["LastName"],
                                create_positions(teacher),
                                teacher["Phone"], teacher["Email"],
                                teacher["TeacherDegree"], teacher["ClassRoom"],
                                create_academic_degrees(teacher)))

    return teachers
