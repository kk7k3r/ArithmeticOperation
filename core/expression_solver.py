from core.based_number import BasedNumber
from core.node import Node


class ExpressionSolver:
    """Класс для выполнения арифметических операций между числами с разными основаниями."""

    OPERATIONS = ['+', '-', '*', '/']

    @staticmethod
    def compute(a: BasedNumber, b: BasedNumber, operation):
        if operation == '+':
            return a.add(b)
        elif operation == '-':
            return a.sub(b)
        elif operation == '*':
            return a.mult(b)
        elif operation == '/':
            return a.div(b)
        else:
            raise ValueError(f"Неизвестная операция: {operation}")

    @staticmethod
    def compute_expression(tree: Node):
        if tree.value in ExpressionSolver.OPERATIONS:
            return ExpressionSolver.compute(
                ExpressionSolver.compute_expression(tree.left),
                ExpressionSolver.compute_expression(tree.right), tree.value)
        return tree.value
