# from random import randint
# m = [randint(0, 10) for _ in range(10)]
# print(m)
# print(m.index(min(m))+1)

# m = []
# prod = 1
# while True:
#     n = input("Введите число или 0 чтобы завершить: ")
#     if n.isdigit():
#         n = int(n)
#         if n == 0:
#             break
#         m.append(n)
#         prod *= n
#         print("Число,", n, "учтеться")
#     else:
#         print("Вводите числа!")
# print(f"Сумма всех элементов списка: {sum(m)}")
#
# if m == []:
#     print("Среднее всех элементов списка: 0")
#     print(f"Произведение всех элементов списка: 0")
# else:
#     print(f"Среднее всех элементов списка: {sum(m) / len(m)}")
#     print(f"Произведение всех элементов списка: {prod}")

# m = []
# while True:
#     n = input("Введите все что угодно или пустую строку чтобы завершить: ")
#     if n == "":
#         break
#     else:
#         m.append(n)
#
# print(min(m, key=len))
# print(max(m, key=len))

# from random import randint
# def random_array_range(start, end):
#     m = []
#     for _ in range(5):
#         m.append(randint(start, end))
#     return m
# m = random_array_range(1, 5)
# for i in range(len(m)):
#     print(f"{i} -> {m[i]};")

# s = input("Введите строку: ")
# print("Start_"+s+"_End", len(s.split()), sep="\n")


# m = [int(i) for i in range(300, 0, -3)]
# print(m)
# print(len(m)) # для проверки

#     for j in range(n):
#         if i != 0 or j != 0:
#            m[i][j] = m[i-1][j] + m[i][j-1]
# for i in m:
# m = [int(i) for i in range(1, 10, 2)]
# print(m)

# n = 5
# m = [[0 for i in range(n)] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0:
#             m[i][j] = 1
# for i in range(n):
#     print(*[f"{x:<3}" for x in i])

# from random import randint
# def medium_temp(m):
#     return [sum(i)/len(i) for i in m]
# m1 = [[randint(1, 35) for _ in range(30)]for _ in range(12)]
# print(m1)
# temperature = medium_temp(m1)
# print(temperature)
# print(sorted(temperature))

# from random import randint
# def medium_temp(d):
#     return {key: round(sum(value)/len(value), 3) for key, value in d.items()}
# mes = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
# temp = [[[randint(1, 35) for _ in range(30)]for _ in range(12)]]
# d = dict(zip(mes, *temp))
# print(d)
# print(medium_temp(d))


# from random import randint
# quantity_tickets = randint(1, 5)
# with open('input.txt', 'w') as f:
#     print(" ".join([str(randint(1, 32)) for _ in range(10)]), file=f)
#     print(str(quantity_tickets), file=f)
#     [print(" ".join([str(randint(1, 32)) for _ in range(6)]), file=f) for _ in range(quantity_tickets)]
# with open('input.txt', 'r') as f:
#     mul_win = {int(i) for i in f.readline().split()}
#     f.readline()#для пропуска ненужной строки
#     with open('output.txt', 'w') as f2:
#         for _ in range(quantity_tickets):
#             mul_fortuna = {int(i) for i in f.readline().split()}
#             print("Lucky" if len([1 for i in mul_fortuna if i in mul_win]) >= 3 else "UnLucky", file=f2)

# with open('nums.txt', 'r') as f:
#     m = [i for i in f.readline().split() if int(i) % 2 != 0]
#     with open('nums.txt', 'w+') as f:
#         print(" ".join(m), file=f)

# with open('waterNums.txt', 'r') as f:
#     mx_s = 0
#     a_and_b = (0, 0)
#     height = [int(i) for i in f.readline().split()]
#     ln = 0
#     for i in range(len(height)):
#         for j in range(i, len(height)):
#             if min(height[i], height[j])*(j-i) > mx_s:
#                 mx_s = min(height[i], height[j])*(j-i)
#                 a_and_b = (height[i], height[j])
#                 ln = j-i
#     print(f"Наибольшая площадь {mx_s}, от высот {a_and_b[0]} и {a_and_b[1]}, на расстоянии {ln}")


# n = 5
# answer = 1
# for i in range(1, n+1):
#     if i % 3 == 0:
#         answer *= i
# print(answer if n != 0 else 0)

# with open('numTask2.txt', 'r') as f:
#     sm = 0
#     m = [float(i) for i in f.readline().split("; ")]
#     for i in m:
#         if i != 0:
#             sm += i
#         else:
#             break
#     print(round(sm, 3))

# with open('numTask3.txt', 'r') as f:
#     m = [int(i) for i in f.readline().split(", ")]
#     print(round(min(m[:m.index(0)])/max(m[:m.index(0)]), 3))

# with open('numTask4.txt', 'r') as f:
#     counter = 0
#     m = [int(i) for i in f.readline().split()]
#     for i in range(len(m)-1):
#         if m[i] == m[i+1]:
#             counter += 1
#     print(counter)

# x_range = (-1.0, 3.0)
# y_range = (-2.0, 4.0)
# point = (0.0, 1.0) # (x, y)
# condition = 'Пинадлежит' if x_range[0]<=point[0]<=x_range[1] and y_range[0]<=point[1]<=y_range[1] else 'Не принадлежит'
# print(f"Точка A{point} {condition} диапозону заштрихованного квадрата")

# def area(x1, y1, x2, y2, x3, y3):
#     return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
# def is_point_in_triangle(a, b):
#     x1, y1 = 0, 2
#     x2, y2 = -2, -3
#     x3, y3 = 2, -3
#     A = area(x1, y1, x2, y2, x3, y3)
#     A1 = area(a, b, x2, y2, x3, y3)
#     A2 = area(x1, y1, a, b, x3, y3)
#     A3 = area(x1, y1, x2, y2, a, b)
#     return A == A1 + A2 + A3
# a = 1.0
# b = -0.8
# if is_point_in_triangle(a, b):
#     print("Точка принадлежит заштрихованной области.")
# else:
#     print("Точка не принадлежит заштрихованной области.")


# with open('numsTask1.txt', 'r') as f:
#     answer = 1
#     m = [int(i) for i in f.readline().split()]
#     for i in m[m.index(min(m))+1:]:
#         answer *= i
#     print(answer)

# def my_sort_arr(m):
#     n = len(m)
#     for i in range(n):
#         for j in range(n - 1):
#             if m[j] > m[j + 1]:
#                 m[j], m[j + 1] = m[j + 1], m[j]
#     return m
# with open('numsTask2.txt', 'r') as f1:
#     m = [float(i) for i in f1.readline().split("; ")]
#     with open('numsTask2.txt', 'w') as f2:
#         print('; '.join([str(i) for i in my_sort_arr(m)]), file=f2)

# with open('numsTask3.txt', 'r') as f:
#     m = [int(i) for i in f.readline().split()]
#     m = [i for i in m[:m.index(min(m))]]
#     print(sum(m)/len(m))

# with open('numsTask4.txt', 'r') as f:
#     m = [int(i) for i in f.readline().split()]
#     m = [i for i in m if i == max(m)-1]
#     print(sum(m))

# with open('numsTask5.txt', 'r') as f:
#     m = [int(i) for i in f.readline().split()]
#     if m.index(min(m)) < m.index(max(m)):
#         m = [i for i in m[m.index(min(m)): m.index(max(m))]]
#     elif m.index(min(m)) > m.index(max(m)):
#         m = [i for i in m[m.index(max(m))+1: m.index(min(m))]]
#     print(*m)# для проверки
#     print(sum(m)/len(m))


# with open('numsTask1.txt', 'r') as f:
#     for line in f:
#         m = [i for i in line.split() if len(i) % 2 != 0]
#         print(*m)

# with open('numsTask2.txt', 'r') as f:
#     [print(line[:-1], end=" ") for line in f.readlines()]

# number = 777
# print(f"Число {number}: {'кратно' if number%10==0 else 'не кратно'} 10 и 2")

# a = 4
# num = int(input("Введите число: "))
# answer = 0
# while num >= 0:
#     answer += num if num%a==0 else 0
#     num = int(input("Введите число: "))
# print(answer)

# from random import randint
# n = 3
# m = 4
# a = [[randint(0, 1) for _ in range(m)] for _ in range(n)]
# [print(*i) for i in a]
# print("-"*9)
# for i in a:
#     i.append(1 if sum(i)%2==1 else 0)
# [print(*i) for i in a]

# from random import uniform
# m_main = [round(uniform(-10.0, 10.0), 3) for _ in range(10)]
# print(f"Наш массив {m_main}")
# m_pls, m_mns = [i for i in m_main if i>0], [i for i in m_main if i<0]
# print("Полученные массивы", m_pls, m_mns, sep="\n")

