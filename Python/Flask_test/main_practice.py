from flask import Flask, request

from main_practice.DTOs.department import Department
from main_practice.DTOs.group import Group
from main_practice.DTOs.student import Student

app = Flask(__name__)

g = Group()
d = Department()


@app.get("/students")
def get_students():
    return {
        "result": "OK",
        "payload": g.get_all_students()
    }


@app.post("/students")
def create_student():
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]

    g.add_student(Student(first_name, last_name))

    return {
        "result": "OK",
        "payload": ""
    }


@app.get("/get-department-specialty-students")
def get_students():
    return {
        "result": "OK",
        "payload": g.get_all_students()
    }


if __name__ == '__main__':
    app.run(debug=True)
