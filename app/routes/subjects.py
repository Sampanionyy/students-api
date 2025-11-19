from flask import Blueprint, jsonify, request
from data.mocks import subjects

subjects_bp = Blueprint('subjects', __name__)

@subjects_bp.route('/', methods=['GET'])
def get_subjects():
    return jsonify(subjects)

@subjects_bp.route('/<int:subject_id>', methods=['GET'])
def get_subject(subject_id):
    subject = next((s for s in subjects if s["id"] == subject_id), None)
    if not subject:
        return jsonify({"error": "Subject not found"}), 404
    return jsonify(subject)

@subjects_bp.route('/', methods=['POST'])
def create_subject():
    data = request.get_json()
    new_subject = {"id": len(subjects) + 1, "name": data["name"]}
    subjects.append(new_subject)
    return jsonify(new_subject), 201
