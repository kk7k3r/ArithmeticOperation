import random
from core.based_number import BasedNumber


class RandomExpressionGenerator:
    def __init__(self):
        self.operations = ['+', '-', '*', '/']
        self.max_depth = 5  # Максимальная глубина дерева

    def get_random_operation(self):
        """Получение случайной операции"""
        return random.choice(self.operations)

    @staticmethod
    def get_random_number():
        """Получение случайного числа"""
        base = random.randint(2, 10)
        num = random.randint(-100, 100)
        value = format(num if num >= 0 else (1 << 8) + num, f'0{base}').lower();
        return BasedNumber(value, base)

    @staticmethod
    def choice(seq):
        """Функция для выбора случайного элемента из списка"""
        return random.choice(seq)

    def generate_expression(self):
        pass
