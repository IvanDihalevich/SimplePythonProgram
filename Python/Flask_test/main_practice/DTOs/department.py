from main_practice.DTOs.specialty import Specialty
from main_practice.DTOs.student import Student


class Department:
    __specialty: list[Specialty] = []

    def get_all_students(self):
        return list(map(lambda s: {"first_name": s.first_name, "last_name": s.last_name}, self.__specialty))

    def delete_specialty(self, specialty_id: int):
        self.__specialty = list(filter(lambda x: x.id != specialty_id, self.__specialty))

    def get_specialty(self):
        return list(map(lambda s: {"name": s.name, "description": s.description}, self.__specialty))

    def add_specialty(self, specialty: Specialty):
        self.__specialty.append(specialty)

    def add_student_to_specialty(self, specialty_name: str, student: Student):
        list(filter(lambda x: x.name == specialty_name, self.__specialty))[0].add_student(student)

