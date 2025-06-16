# Задание 2. Дана целочисленная последовательность. Извлечь из нее все положительные
# числа;
nums_order = '5 -3 21 -4 2 0'
arr_nums_order = nums_order.split()
arr_nums_positive_order = [i for i in arr_nums_order if i > '0']
nums_positive_order = ' '.join(arr_nums_positive_order)
print(nums_positive_order)