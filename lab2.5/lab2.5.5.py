"""Задание 5. Напишите функцию для вычисления значения выражения (a+4b)(a−3b)+a2;"""


def answer_for_exam(a: int, b: int):
    return (a+4*b)*(a-3*b)+2*a


print(answer_for_exam(1, 1))