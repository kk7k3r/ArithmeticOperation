from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from Core.RandomExpressionGenerator import RandomExpressionGenerator

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
    expression = expression_generator.generate_expression()
    correct_answer = 1
    base=10
    return jsonify({
        "equation": str(expression),
        "correctAnswer": str(correct_answer),
        "base": base
    })

@controllers.route('/check_answer', methods=['POST'])
def check_answer():
    pass