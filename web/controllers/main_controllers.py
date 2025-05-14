from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from core.random_expression_generator import RandomExpressionGenerator
from core.expression_renderer import ExpressionRenderer
from core.expression_solver import ExpressionSolver
import os
from flask import send_from_directory
from datetime import datetime

controllers = Blueprint("controllers", __name__)


@controllers.route('/')
def index():
    """
    Отображает главную страницу приложения.

    Returns:
        HTML-страница index.html.
    """
    return render_template('index.html')


@controllers.route('/generate', methods=['POST'])
def generate_expression():
    """
    Генерирует случайное арифметическое выражение и вычисляет правильный ответ.

    Ожидает JSON с параметрами:
        name (str): имя пользователя.
        tries (int): количество попыток.

    Returns:
        JSON:
            equation (str): представление выражения.
            correctAnswer (float): правильный ответ
            base (int): основание системы счисления (пока что всегда 10).
    """
    data = request.get_json()
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
    """
    Проверяет, совпадает ли ответ пользователя с правильным ответом.

    Ожидает JSON с параметрами:
        answer (str): ответ пользователя.
        correct_answer (str): правильный ответ.

    Returns:
        JSON:
            correct (bool): True, если ответ верный, иначе False.
    """
    data = request.json
    user_answer = data.get("answer")
    correct_answer = data.get("correct_answer")
    try:
        result = float(user_answer) == float(correct_answer)
    except Exception:
        result = str(user_answer) == str(correct_answer)
    return jsonify({"correct": result})


@controllers.route('/save_result', methods=['POST'])
def save_result():
    """
    Сохраняет результаты попыток пользователя в текстовый файл на сервере.

    Ожидает JSON с параметрами:
        table (str): текст таблицы с результатами.
        surname (str): фамилия пользователя.
        comment (str): комментарий пользователя.
        time (str): время сохранения.

    Returns:
        JSON:
            status (str): "ok" при успешном сохранении.
            filename (str): имя сохранённого файла.
    """
    data = request.json
    table = data.get('table')
    surname = data.get('surname')
    comment = data.get('comment')
    time = data.get('time')
    content = f"{table}\n{time}\t{surname}\t{comment}\n"
    os.makedirs('results', exist_ok=True)
    filename = f"{surname}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join('results', filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return jsonify({"status": "ok", "filename": filename})


@controllers.route('/download_result/<filename>')
def download_result(filename):
    """
    Позволяет скачать ранее сохранённый файл с результатами.

    Args:
        filename (str): имя файла для скачивания.

    Returns:
        Файл для скачивания
    """
    return send_from_directory('results', filename, as_attachment=True)
