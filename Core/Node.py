class Node:
    """Класс для представления узла дерева"""
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(f"{str(self.left)} {self.value} {str(self.right)}")