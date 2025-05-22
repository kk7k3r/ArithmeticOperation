class BasedNumber:
    """
       Класс для представления числа в произвольной системе счисления.
    """

    def __init__(self, value, base):
        """
            Инициализация числа.

            Args:
                value (str|int): Значение числа в виде строки или числа.
                base (int): Основание системы счисления.
        """
        self.value = value
        self.base = base

    def add(self, other):
        """
            Складывает два числа, возвращает результат в десятичной системе.
        """
        val1, val2 = self.convert_values(other)
        return BasedNumber(val1 + val2, 10)

    def sub(self, other):
        """
            Вычитает из текущего числа число, переданное в параметре,
            возвращает результат в десятичной системе.
        """
        val1, val2 = self.convert_values(other)
        return BasedNumber(val1 - val2, 10)

    def mult(self, other):
        """
            Умнажает два числа,
            возвращает результат в десятичной системе.
        """
        val1, val2 = self.convert_values(other)
        return BasedNumber(val1 * val2, 10)

    def div(self, other):
        """
            Делит текущее чесло на число, переданное в параметре,
            возвращает результат в десятичной системе.
        """
        val1, val2 = self.convert_values(other)
        if val2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return BasedNumber(val1 // val2, 10)

    def convert_values(self, other):
        """
            Преобразует оба числа к десятичному виду.
        """
        return [self.to_decimal(), other.to_decimal()]

    def to_decimal(self):
        """
            Переводит число в десятичную систему.

            Returns:
                int: Значение в десятичной системе.
        """
        val_str = str(self.value)
        negative = val_str.startswith('-')
        val_str = val_str[1:] if negative else val_str

        decimal_value = int(val_str, self.base)
        return -decimal_value if negative else decimal_value

    @staticmethod
    def from_decimal(value: int, base: int):
        """
            Создаёт объект BasedNumber из десятичного числа и основания.

            Args:
                value (int): Значение в десятичной системе.
                base (int): Основание системы счисления.

            Returns:
                BasedNumber: Число в заданной системе.
        """
        digits = []
        is_negative = value < 0
        value = abs(value)
        if value == 0:
            return BasedNumber('0', base)
        while value > 0:
            digits.append("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[value % base])
            value //= base
        digits.reverse()
        s = ''.join(digits)
        return BasedNumber('-' + s if is_negative else s, base)