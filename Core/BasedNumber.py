class BasedNumber:
    def __init__(self, value, base):
        self.value = value
        self.base = base

    def add(self, other):
        val1, val2 = self.convertValues(other)
        return BasedNumber(val1 + val2, 10)

    def sub(self, other):
        val1, val2 = self.convertValues(other)
        return BasedNumber(val1 - val2, 10)

    def mult(self, other):
        val1, val2 = self.convertValues(other)
        return BasedNumber(val1 * val2, 10)

    def div(self, other):
        val1, val2 = self.convertValues(other)
        if val2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return BasedNumber(val1 / val2, 10)

    def convertValues(self, other):
        return [self.toDecimal(), other.toDecimal()]

    def toDecimal(self):
        if self.base != 10 or isinstance(self.value, str):
            return int(self.value), int(self.base)
        return self.value

    def __str__(self):
        return f"<span>{self.value}</span><sub>{self.base}</sub>)"