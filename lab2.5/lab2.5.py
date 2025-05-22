# n1 = 1
# n2 = int(input("До какого числа перебор включительно: "))
# counter = 0
# for i in range(n1, n2+1):
#     counter += i
# print(counter)
from operator import index


def our_func(arr: list):
    counter_positive = 0
    counter_mult = 1
    mn_num = 999
    mx_num = -999
    for item in arr:
        if item > 0:
            counter_positive += item
        if item > mx_num:
            mx_num = item
        if item < mn_num:
            mn_num = item
    mn_index, mx_index = sorted((index(mn_num), index(mx_num)))
    for i in range(mn_index, mx_index+1):
        counter_mult *= arr[i]
    return counter_positive, counter_mult
print(our_func([2, 3, -2]))

# from random import randrange
# def get_random_arr(len_arr, range_num):
#     arr = []
#     for _ in range(len_arr):
#         arr.append(randrange(0, range_num, 2))
#     return sorted(arr)
# print(get_random_arr(5, 100))

# our_string = "abcxxx"
# if our_string.startswith("abc"):
#     print("www" + our_string[3:])
# else:
#     print(our_string + "zzz")

#  Напишите функцию для вычисления значения выражения (a+4b)(a−3b)+a2;
# def answer_for_exam(a: int, b: int):
#     return (a+4*b)*(a-3*b)+2*a
# print(answer_for_exam(1, 1))

# our_arr = [-2, -1, 0, 1, 2]
# print(our_arr)
# for i, item in enumerate(our_arr):
#     our_arr[i] = item * -1
# print(our_arr)

# point = (2, -2)
# rad = 2.83
# c = (point[0]**2 + point[1]**2)**0.5
# if c <= rad:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

