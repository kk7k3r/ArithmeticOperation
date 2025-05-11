from Core import BasedNumber, Node


class OperationSolver:
    """Класс для выполнения арифметических операций между числами с разными основаниями."""

    def __init__(self):
        self.operations = ['+', '-', '*', '/']

    def compute(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b
        else:
            raise ValueError(f"Неизвестная операция: {self.op}")

    def computeExpression(self, tree: Node):
        if tree.value in self.operations:
            return self.compute(
                self.computeExpression(tree.left),
                self.computeExpression(tree.right), tree.value)
        return tree.value
