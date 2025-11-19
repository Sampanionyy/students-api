from flask import Blueprint, jsonify, request
from data.mocks import students

students_bp = Blueprint('students', __name__)

@students_bp.route('/', methods=['GET'])
def get_students():
    return jsonify(students)

@students_bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student)

@students_bp.route('/', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = {"id": len(students) + 1, "name": data["name"]}
    students.append(new_student)
    return jsonify(new_student), 201
