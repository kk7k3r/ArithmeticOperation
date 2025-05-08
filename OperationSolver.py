import BasedNumber


class OperationSolver:
    """Класс для выполнения арифметических операций между числами с разными основаниями."""

    def __init__(self, a: BasedNumber, b: BasedNumber, op: str):
        self.a = a
        self.b = b
        self.op = op

    def compute(self):
        a_dec = self.a.to_decimal()
        b_dec = self.b.to_decimal()

        if self.op == '+':
            return a_dec + b_dec
        elif self.op == '-':
            return a_dec - b_dec
        elif self.op == '*':
            return a_dec * b_dec
        elif self.op == '/':
            return a_dec / b_dec
        else:
            raise ValueError(f"Неизвестная операция: {self.op}")