class Node:
    """
        Создаёт объект BasedNumber из десятичного числа и основания.

        Args:
            value (int): Значение в десятичной системе.
            base (int): Основание системы счисления.

        Returns:
            BasedNumber: Число в заданной системе.
        """

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return (f"{str(self.left) if self.left is not None else ''} "
                f"{self.value} {str(self.right) if self.right is not None else ''}")
