from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from data.mocks import students, global_stats, QUIZ_CATEGORIES, QUIZ_QUESTIONS
import random
from datetime import datetime

quiz_bp = Blueprint('quiz', __name__)


@quiz_bp.route('/quiz')
def quiz_home():
    # Trier les étudiants par score
    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
    return render_template('quiz_home.html', 
                         categories=QUIZ_CATEGORIES, 
                         students=sorted_students,
                         stats=global_stats)

@quiz_bp.route('/quiz/play/<category>')
def quiz_play(category):
    if category not in QUIZ_CATEGORIES:
        return "Category not found", 404
    
    student_id = request.args.get('student_id', type=int)
    student = next((s for s in students if s["id"] == student_id), None)
    
    if not student:
        return redirect(url_for('quiz.quiz_home'))
    
    questions = QUIZ_QUESTIONS.get(category, [])
    
    # Store quiz session
    session['quiz_category'] = category
    session['quiz_student_id'] = student_id
    session['quiz_started'] = True
    session['quiz_start_time'] = datetime.now().isoformat()
    
    return render_template('quiz_play.html', 
                         category=QUIZ_CATEGORIES[category],
                         questions=questions,
                         student=student,
                         total_questions=len(questions))

@quiz_bp.route('/quiz/submit', methods=['POST'])
def quiz_submit():
    category = session.get('quiz_category')
    student_id = session.get('quiz_student_id')
    
    if not category or not student_id:
        return "Session invalide", 400
    
    student = next((s for s in students if s["id"] == student_id), None)
    questions = QUIZ_QUESTIONS.get(category, [])
    
    score = 0
    answers = []
    
    for q in questions:
        user_answer = request.form.get(f"question_{q['id']}")
        is_correct = user_answer == q["answer"]
        if is_correct:
            score += 1
        
        answers.append({
            "question": q["question"],
            "user_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct
        })
    
    # Calculer le pourcentage
    percentage = int((score / len(questions)) * 100)
    
    # Calculer les points gagnés (10 points par bonne réponse)
    points_earned = score * 10
    
    # Clear session
    session.pop('quiz_category', None)
    session.pop('quiz_student_id', None)
    session.pop('quiz_started', None)
    session.pop('quiz_start_time', None)
    
    return render_template('quiz_result.html', 
                         student=student,
                         category=QUIZ_CATEGORIES[category],
                         score=score,
                         total=len(questions),
                         percentage=percentage,
                         points_earned=points_earned,
                         answers=answers)

# API pour obtenir les statistiques
@quiz_bp.route('/api/leaderboard')
def api_leaderboard():
    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
    return jsonify(sorted_students)