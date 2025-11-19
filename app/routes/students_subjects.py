from flask import Blueprint, jsonify, request
from data.mocks import students, subjects, students_subjects

students_subjects_bp = Blueprint('students_subjects', __name__)

@students_subjects_bp.route('/', methods=['GET'])
def get_all_relations():
    return jsonify(students_subjects)

@students_subjects_bp.route('/', methods=['POST'])
def add_relation():
    data = request.get_json()
    student_id = data.get("student_id")
    subject_id = data.get("subject_id")

    # Basic validations
    if not any(s["id"] == student_id for s in students):
        return jsonify({"error": "Student not found"}), 404
    if not any(s["id"] == subject_id for s in subjects):
        return jsonify({"error": "Subject not found"}), 404

    new_relation = {"student_id": student_id, "subject_id": subject_id}
    students_subjects.append(new_relation)
    return jsonify(new_relation), 201
