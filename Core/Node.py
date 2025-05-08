class Node:
    """Класс для представления узла дерева"""
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None