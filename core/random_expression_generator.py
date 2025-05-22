import random
from core.based_number import BasedNumber
from core.node import Node


class RandomExpressionGenerator:
    def __init__(self, max_depth=3):
        """
            Args:
                max_depth (int): Максимальная глубина дерева выражения.
        """
        self.operations = ['+', '-', '*', '/']
        self.max_depth = max_depth  # Максимальная глубина дерева

    def get_random_operation(self):
        """Генерация случайной операции"""
        return random.choice(self.operations)

    @staticmethod
    def get_random_number():
        """Генерация случайного числа"""
        base = random.randint(2, 10)
        value = random.randint(-100, 100)
        return BasedNumber.from_decimal(value, base)

    @staticmethod
    def choice(seq):
        """Функция для выбора случайного элемента из списка"""
        return random.choice(seq)

    def generate_expression_tree(self, depth=1):
        """
           Рекурсивно создаёт дерево выражения, где:
           - внутренние узлы — операции
           - листья — числа в случайной системе счисления
           """
        if depth > self.max_depth:
            return Node(self.get_random_number())

        node = Node(self.get_random_operation())

        if random.choice(['operation', 'number']) == 'operation' and depth < self.max_depth:
            node.left = self.generate_expression_tree(depth + 1)
        else:
            node.left = Node(self.get_random_number())

        if random.choice(['operation', 'number']) == 'operation' and depth < self.max_depth:
            node.right = self.generate_expression_tree(depth + 1)
        else:
            node.right = Node(self.get_random_number())

        return node
