from main_practice.DTOs.student import Student

id = 1


class Specialty:
    __students: list[Student] = []

    def __init__(self, name, description):
        self.id = id + 1
        self.name = name
        self.description = description
        id += 1

    def get_students(self):
        return self.__students

    def delete_student(self, student_id: int):
        self.__students = list(filter(lambda x: x.id != student_id, self.__students))

    def add_student(self, student: Student):
        self.__students.append(student)
