"""Задание 3. Сформируйте возрастающий массив из случайных четных чисел;"""
from random import randrange


def get_random_arr(len_arr, range_num):
    arr = []
    for _ in range(len_arr):
        arr.append(randrange(0, range_num, 2))
    return sorted(arr)


print(get_random_arr(5, 100))