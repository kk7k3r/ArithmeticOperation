﻿from core.based_number import BasedNumber
from core.node import Node


class ExpressionRenderer:
    OPERATOR_PRECEDENCE = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    @staticmethod
    def render(expression_tree: Node, parent_precedence=0):
        """
        Рекурсивно строит выражение из дерева node.
        :param expression_tree: экземпляр Node
        :param parent_precedence: приоритет родительской операции
        :return: строка выражения
        """
        if expression_tree is None:
            return ''

        if not isinstance(expression_tree.value,
                          str) or expression_tree.value not in ExpressionRenderer.OPERATOR_PRECEDENCE:
            return ExpressionRenderer.render_based_number(expression_tree.value)

        current_op = expression_tree.value
        current_precedence = ExpressionRenderer.OPERATOR_PRECEDENCE.get(current_op, 0)

        left_expr = ExpressionRenderer.render(expression_tree.left, current_precedence)
        right_expr = ExpressionRenderer.render(expression_tree.right, current_precedence)

        expr = f"{left_expr} {current_op} {right_expr}"

        if current_precedence < parent_precedence:
            return f"({expr})"
        return expr

    @staticmethod
    def render_based_number(number: BasedNumber):
        result = f"<span>{number.value}</span><sub>{number.base}</sub>"
        if str(number.value).startswith("-"):
            result = f"({result})"
        return result
