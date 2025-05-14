from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from core.random_expression_generator import RandomExpressionGenerator
from core.expression_renderer import ExpressionRenderer
from core.expression_solver import ExpressionSolver
controllers = Blueprint("controllers", __name__)


@controllers.route('/')
def index():
    return render_template('index.html')


@controllers.route('/generate', methods=['POST'])
def generate_expression():
    data = request.get_json()
    name = data.get('name')
    tries = int(data.get('tries'))
    expression_generator = RandomExpressionGenerator()
    expression_tree = expression_generator.generate_expression_tree()
    expression = ExpressionRenderer.render(expression_tree)
    correct_answer = ExpressionSolver.compute_expression(expression_tree)
    base = 10
    return jsonify({
        "equation": expression,
        "correctAnswer": correct_answer.value,
        "base": base
    })

@controllers.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data.get("answer")
    correct_answer = data.get("correct_answer")
    try:
        result = float(user_answer) == float(correct_answer)
    except Exception:
        result = str(user_answer) == str(correct_answer)
    return jsonify({"correct": result})
