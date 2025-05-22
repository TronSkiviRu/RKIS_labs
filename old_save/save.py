#**** 1

# m = int(input())
# print(f"Distance in centimeters: {m*100}")

# km, m = float(input("Введите в км: ")), float(input("Введите в метрах: "))
# if m < km*1000:
# print(m, "-- метров меньше")
# elif km*1000 < m:
# print(km*1000, "-- км в переводе в метры меньше")
# else:
# print("Равны")

# num = int(input())
# for i in range(10):
#     print(f"{num} * {i} = {num * i}")

#**** 2

# a, b = int(input("число а = ")), int(input("число б = "))
# if a % b == 0:
#     print("Является делителем")
# else:
#     print("Не является делителем")

# print("That`s the number you entered", int(input("Введи любое число ")))

# print("Введи числа m и n")
# m, n = int(input()), int(input())
# if m > n:
#   print("Number m > n")
# elif m < n:
#   print("Number m < n")
# else:
#   print("The numbers are equal")

# inp = int(input("Введи радиус окружности: "))
# print("Вот её диаметр", inp*2)

# print("Сумма всех чисел от 100 до 500: ", sum(list(range(100, 500))))
# inp = int(input("Введи а(a<500): "))
# print("Сумма всех чисел от a до 500: ", sum(list(range(inp, 500))))

#**** 3

# print("Hello!", input("Как тебя зовут? "))

# print("Вводи числа a, b, c")
# a, b, c = int(input()), int(input()), int(input())
# m = max([a, b, c])
# print("Cамое большое: ", m)

# a, b = int(input("Число а ")), int(input("Число b "))
# a, b = b, a
# print(f"a= {a} b= {b}")

# l = [1, 2, 66, -1, 0, 777]
# print(l.index(min(l)))

# def kb_to_b(n):
# return n*1024
# def b_to_kb(n):
# return n/1024
# n = int(input("какую функцию выберете? 0 - кб в байты или 1 - байты в кб: "))
# num = float(input("введи значение: "))
# print([f"{kb_to_b(num)} байт", f"{b_to_kb(num)} Kb"][n])

#**** 4

# inp = input("Введите натуральное число: ")
# n = list(map(int, list(inp)))
# m = 1
# for i in n:
#     m *= i
# print(sum(n), m)

# from random import randint
# a = int(input("Начало диапозона: "))
# b = int(input("Конец диапозона: "))
# c = int(input("кол-во элементов: "))
# def random_list(a, b, l):# l -длина
#     return [randint(a, b) for _ in range(l)]
# print(random_list(a, b, c))

# from random import randint
# def gen_l():
#     l = [randint(-100, 100) for _ in range(10)]
#     print(l)
#     p1 = len([i for i in l if i > 0])
#     p2 = len([i for i in l if i < 0])
#     p3 = len([i for i in l if i == 0])
#     print(f"{p1}(+), {p2}(-), {p3}(0)")
# gen_l()

# from random import randint
# m1 = [[randint(-100, 100), randint(-100, 100)] for _ in range(10)]
# def mx(m1):
#     return [max(i) for i in m1]
# [print(*i) for i in m1]
# print(mx(m1))

# m = [ [[3, 2, 1], [5, 8], [9, 4, 6, 0]], [[5, 4, 5], [9, 1]], [[6, 7, 8], [9, 0]] ]
# print("Наш массив", m, "его индексы младших массивов", sep="\n")
# for i in range(len(m)):
#     for lab2.5 in range(len(m[i])):
#         print(f"{i} {lab2.5} {m[i][lab2.5].index(min(m[i][lab2.5]))}")

#**** 5

# m = [9, 5, 1]
# target = 10
# for i in range(len(m)):
#     for lab2.5 in range(i + 1, len(m)):
#         if m[i] + m[lab2.5] == target:
#             print(f"{i} {lab2.5}")

# num = 4537
# print(int(str(num)[::-1]))

# n = int(input())
# print( str(n) == str(n)[::-1] )

# m1, m2 = [1, 3, 5], [2, 4, 6]
# m = m1 + m2
# f = 0
# print(m, "было")
# while True:
#     for i in range(len(m)-1):
#         if m[i] > m[i+1]:
#             m[i], m[i+1] = m[i+1], m[i]
#             f += 1
#     if f == 0:
#         break
#     else:
#         f = 0
# print(m, "стало")

# m = [1, 3, 4, 5, 6, 7]
# target = 90
# if target <= max(m):
#     print([m.index(i) for i in m if i >= target][0])
# else:
#     print(m.index(max(m))+1)

#**** 6

# from datetime import *
# name_week = datetime.today().strftime('%B')
# name_month = datetime.today().strftime('%A')
# print(name_week, name_month, "Igor", sep="\n")

# n1, n2, n3 = [int(input()) for i in range(3)]
# n1 *= 2
# n2 -= 3
# n3 **= 2
# print(n1+n2+n3)

# def number_squares(a, b, l):
#     a_correct = a // l
#     b_correct = b // l
#     return a_correct * b_correct
# print(number_squares(8, 3, 3))

# def mx(n1, n2):
#     if n1 < n2: return n2
#     elif n1 > n2: return n1
#     else: return "Они равны!"
# print(mx(9, 3))

# def number_positive(m):
#     return len([i for i in m if i > 0])
# print(number_positive([9, 1, 0, -1, -99, 99]))

# n = "12345"
# def not_even_product(n):
#     ans = 1
#     for i in n[::-2]:
#         ans *= int(i)
#     return ans
# print(not_even_product(n))

# n = 963
# def check(num):
#     num = str(num)
#     a = len([1 for i in range(len(num)-1) if num[i] > num[i+1]])
#     b = len(num) - 1
#     return ["Не по убыванию", "По убыванию"][a==b]
# print(check(n))

# from random import randrange, randint
# m = []
# step_for_ran = [930, 990]
# for i in range(randint(1, 23), 25):
#     n = randrange(step_for_ran[0], step_for_ran[1], 3)
#     m.append(n)
#     step_for_ran[0] -= 90
#     step_for_ran[1] -= 90
# print(m)

# m = [8, 0, 3, 5, 6, 0]
# x = 1
# print(["Нету", "Есть"][x in m])

# m = [[3, 3, 3], 3, 4, [5, 6, 7, 8], 2, [7, 7, 7, [4, 4, 4, 4], [7, 7, 7, 7, [8, 8, 8, 8, [9]], 2], 2], 2]
# def processing_array(m):
#     for i in range(len(m)):
#         if isinstance(m[i], list):
#             m[i] = processing_array(m[i])
#         else:
#             m[i] **= i
#     return m
# for i in range(len(m)):
#     if isinstance(m[i], list):
#         processing_array(m[i])
#     else:
#         m[i] **= i
# print(m)


#**** 2.1

# l = [1, 2, 3, 4, 5]
# print(l)
# print(l[::-1])

# l = [1, 2, 3, 4, 5]
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
# print(l)
# print(change(l))

# def to_list(*args):
#     return list(args)
# print(to_list((), 1, "бульба", 3.0, {}))

# seq = "0123123233"
# def count_it(sequence):
#     d = {}
#     for i in sequence:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     return dict(sorted(d.items(), key=lambda i: i[1], reverse=True)[:3])
# print(count_it(seq))

# l = [1, 2, 1, 2, 3]
# def sieve(l):
#     tup = []
#     for i in l:
#         if i not in tup:
#             tup.append(i)
#     return tuple(tup[::-1])
# print(sieve(l))

# def season_events(number_of_month):
#     if number_of_month in ('12', '1', '2'):
#         s1 = "Зимой"
#         s2 = "За окном падал белый снег"
#     elif number_of_month in ('3', '4', '5'):
#         s1 = "Весной"
#         s2 = "Птицы пели прекрасные песни"
#     elif number_of_month in ('6', '7', '8'):
#         s1 = "Летом"
#         s2 = "Солнце светило ярче, чем когда-либо"
#     elif number_of_month in ('9', '10', '11'):
#         s1 = "Осенью"
#         s2 = "Урожай был невероятным"
#     else:
#         return print("Не вверный ввод в функцию")
#     print(f"Вы родились {s1}. {s2}.")
#
# n = input("Введите номер месяца: ")
# season_events(n)

# strings = [
#     "http://example.com",
#     "https://secure-site.com",
#     "ftp://files.com",
#     "http://another-example.com",
#     "just-a-string",
#     "http://http://.com",
#     "jijhttp://"
# ]
# filtered_strings = [s for s in strings if s.startswith("http://")]
# print(filtered_strings)

# import time
# date_str = '2025-12-12'
# time_struct = time.strptime(date_str, '%Y-%m-%d')
# date_dict = {
#     'year': str(time_struct.tm_year),
#     'month': str(time_struct.tm_mon).zfill(2),  # Месяц (с нулем впереди)
#     'day': str(time_struct.tm_mday).zfill(2),
# }
# print(date_str)
# print(date_dict)

#**** 2.2

# import random
# numbers = [random.randint(1, 100) for _ in range(10)]
# print("Случайные числа:", numbers)
# min_number = min(numbers)
# print("Минимальный элемент коллекции:", min_number)

# def greet():
#     print("Welcome")
# greet()

# def greet_with_name(name):
#     print(f"Hello, {name}")
# greet_with_name("Ababek")

# def multiply(a, b):
#     return a * b
# result = multiply(5, 3)
# print("Произведение:", result)

# def meters_to_kilometers(meters):
#     return meters / 1000
# kilometers = meters_to_kilometers(1500)
# print("Километры:", kilometers)

# def is_divisor(a, b):
#     return b % a == 0
# print(is_divisor(3, 9))

# def find_minimum(arr):
#     return min(arr)
# min_element = find_minimum([5, 3, 8, 1, 4])
# print("Минимальный элемент массива:", min_element)

# def diameter_from_radius(radius):
#     return 2 * radius
# diameter = diameter_from_radius(5)
# print("Диаметр:", diameter)

# def max_of_two(a, b):
#     return max(a, b)
# maximum = max_of_two(10, 20)
# print("Наибольшее число:", maximum)

# def find_shortest_and_longest():
#     elements = []
#     while True:
#         element = input("Введите элемент (или пустую строку для завершения): ")
#         if element == "":
#             break
#         elements.append(element)
#     if elements:
#         shortest = min(elements, key=len)
#         longest = max(elements, key=len)
#         print("Самый короткий элемент:", shortest)
#         print("Самый длинный элемент:", longest)
#     else:
#         print("Список пуст.")
# find_shortest_and_longest()


#**** 2.3

# import locale
# import datetime
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# now = datetime.datetime.now()
# day_of_week = now.strftime("%A")
# month_name = now.strftime("%B")
# print(day_of_week)
# print(month_name)
# print("Igorechek")

# n1, n2, n3 = [int(input()) for _ in range(3)]
# n1 *= 2
# n2 -= 3
# n3 **= 2
# print(sum([n1, n2, n3]))

# def counter_quads(a, b, n):
#     return (a//n)*(b//n)
# print(counter_quads(5, 3, 2))

# def max_num_between_two(a, b):
#     return a if a>b else b
# print(max_num_between_two(2, 8))

# def counter_positive_in_array(arr):
#     return len([1 for i in arr if i > 0])
# print(counter_positive_in_array([-1, -0, +0, +94, 2]))

# def mult_not_two(num):
#     answer = 1
#     for i in [item for i, item in enumerate(list(str(num)), 1) if i%2 == 1]:
#         answer *= int(i)
#     return answer
# print(mult_not_two(1234562))

# def is_descending_order(num):
#     s = str(num)
#     condition1 = len([1 for i in range(len(s)-1) if s[i] >= s[i+1]]) + 1
#     condition2 = len(s)
#     return condition1 == condition2
# print(is_descending_order(321))

# from random import randrange
# arr = [randrange(0, 999, 3) for i in range(25)]
# print(arr, len(arr))

# def is_digit_in_array(dig, arr):
#     return dig in arr
# print(is_digit_in_array(1, [1, 2, 3, 4]))

# def create_square_array(size):
#     return [i**2 for i in range(1, size)]
# print(create_square_array(10))

# from random import randint
# arr = []
# for i in range(15):
#     arr.append(randint(10, 99))
# for i in arr:
#     print(i, end=" ")
# print()
# print(len(arr))

# arr = []
# for i in range(14):
#     arr.append(int(input()))
# arr.append(sum(arr))
# for i in arr:
#     print(i, end=" ")
# print()
# print(len(arr))

# def enum(firstNumber, secondNumber, operation):
#     match operation:
#         case "+":
#             result = firstNumber + secondNumber
#         case "-":
#             result = firstNumber - secondNumber
#         case "*":
#             result = firstNumber * secondNumber
#         case "/":
#             result = firstNumber / secondNumber
#         case _:
#             result = "error"
#     return firstNumber, secondNumber, operation, result
# n1, n2, char, answer = enum(1, 2, "banana")
# print(n1, n2, char, answer)

# from datetime import datetime
# import locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# def format_date(input_date):
#     try:
#         date_object = datetime.strptime(input_date, "%d.%m.%Y")
#         day_of_week = date_object.strftime("%A").capitalize()
#         day = date_object.day
#         month = date_object.strftime("%B").capitalize()
#         year = date_object.year
#         formatted_date = f"{day_of_week}, {day} {month}, {year} год"
#         return formatted_date
#     except ValueError:
#         return "Не верный формат!"
# input_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
# output_date = format_date(input_date)
# print(output_date)
