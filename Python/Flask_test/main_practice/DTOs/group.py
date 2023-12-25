from main_practice.DTOs.student import Student


class Group:
    __students: list[Student] = []

    def add_student(self, student: Student):
        self.__students.append(student)

    def get_all_students(self):
        return list(map(lambda x: {"first_name": x.first_name, "last_name": x.last_name}, self.__students))
