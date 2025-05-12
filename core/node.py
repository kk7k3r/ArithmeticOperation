class Node:
    """Класс для представления узла дерева"""

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return (f"{str(self.left) if self.left is not None else ''} "
                f"{self.value} {str(self.right) if self.right is not None else ''}")
