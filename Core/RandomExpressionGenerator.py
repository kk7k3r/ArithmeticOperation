import random
from Core.Node import Node
from Core.BasedNumber import BasedNumber


class RandomExpressionGenerator:
    def __init__(self):
        self.operations = ['+', '-', '*', '/']
        self.max_depth = 5  # Максимальная глубина дерева

    def getRandomOperation(self):
        """Получение случайной операции"""
        return random.choice(self.operations)

    def getRandomNumber(self):
        """Получение случайного числа"""
        base = random.randint(2, 10)
        num = random.randint(-100, 100)
        value = format(num if num >= 0 else (1 << 8) + num, f'0{base}').lower();
        return BasedNumber(value, base)

    def choice(self, seq):
        """Функция для выбора случайного элемента из списка"""
        return random.choice(seq)

    def build_subtree(self, depth, stack):
        child = Node(None)
        if random.choice(['operation', 'number']) == 'operation' and depth <= self.max_depth:
            child.value = self.getRandomOperation()
            stack.append((child, depth + 1))
        else:
            child.value = self.getRandomOperation()
        return child

    def generate_expression(self):
        root = Node(self.getRandomOperation())
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            node.left = self.build_subtree(depth, stack)
            node.right = self.build_subtree(depth, stack)

        return root
