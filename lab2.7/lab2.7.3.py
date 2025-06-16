# Задание 3. Дана целочисленная последовательность. Извлечь из нее все положительные
# двузначные числа, отсортировав их по возрастанию;
nums_order = '6 -3 20 -4 2 0'
arr_nums_order = nums_order.split()
arr_nums_request = []
for i in arr_nums_order:
    int_i = int(i)
    if int_i % 2 == 0 and int_i > 0:
        arr_nums_request.append(int_i)
arr_nums_request.sort()
arr_nums_request = [str(i) for i in arr_nums_request]
nums_request_order = ' '.join(arr_nums_request)
print(nums_request_order)