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

#     for lab2.5 in range(n):
#         if i != 0 or lab2.5 != 0:
#            m[i][lab2.5] = m[i-1][lab2.5] + m[i][lab2.5-1]
# for i in m:
# m = [int(i) for i in range(1, 10, 2)]
# print(m)

# n = 5
# m = [[0 for i in range(n)] for i in range(n)]
# for i in range(n):
#     for lab2.5 in range(n):
#         if i == 0 or lab2.5 == 0:
#             m[i][lab2.5] = 1
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






# import json
# from datetime import datetime, timedelta
#
# TASKS_FILE = 'tasks.json'
#
# def save_tasks(tasks):
#     with open(TASKS_FILE, 'w') as file:
#         json.dump(tasks, file, indent=4)
#
# def main():
#     print("*" + "-" * 25 + "*")
#     print("|" + "Консольный ежедневник".center(25, ' ') + "|")
#     print("|" + "1.Начать".center(25, ' ') + "|")
#     print("|" + "2.Выйти!".center(25, ' ') + "|")
#     print("*" + "-" * 25 + "*")
#     answer1 = input("Решение: ")
#
#     print("\n" * 20)
#
#     if answer1 == "1":
#         print("*" + "-" * 75 + "*")
#         while True:
#             with open(TASKS_FILE, 'r') as file:
#                 tasks = json.load(file)
#
#
#             print(f"Сегодня {(datetime.now().strftime('%d.%m.%Y'))}. Что будем делать?")
#             print("1. Добавить задачу".ljust(25), "3. Редактировать задачу".ljust(25))
#             print("2. Удалить задачу".ljust(25), "4. Просмотреть задачи".ljust(25), end="")
#             print("0. Выйти")
#             answer2 = input("Решение: ")
#             print("\n" * 20)
#
#             if answer2 == "1":
#                 title = input("Введите название задачи: ")
#                 description = input("Введите описание задачи: ")
#                 date = input("Введите дату выполнения задачи (день.месяц.год): ")
#                 task = {
#                     'title': title,
#                     'description': description,
#                     'date': date
#                 }
#                 tasks.append(task)
#                 save_tasks(tasks)
#                 print("\n" * 20)
#                 print("Задача добавлена!")
#
#             elif answer2 == "2":
#                 print("Это ваши задачи!")
#                 for index, task in enumerate(tasks, start=1):
#                     print(f"{index}. {task['title']} - {task['description']} (до {task['date']})")
#                 task_index = int(input("Введите номер задачи для удаления: ")) - 1
#                 if 0 <= task_index < len(tasks):
#                     tasks.pop(task_index)
#                     save_tasks(tasks)
#                     print("\n" * 20)
#                     print("Задача удалена!")
#                 else:
#                     print("\n" * 20)
#                     print("Неверный номер задачи.")
#
#             elif answer2 == "3":
#                 print("Это ваши задачи!")
#                 for index, task in enumerate(tasks, start=1):
#                     print(f"{index}. {task['title']} - {task['description']} (до {task['date']})")
#                 task_index = int(input("Введите номер задачи для редактирования: ")) - 1
#                 if 0 <= task_index < len(tasks):
#                     title = input("Введите новое название задачи (или нажмите Enter для сохранения текущего): ")
#                     description = input("Введите новое описание задачи (или нажмите Enter для сохранения текущего): ")
#                     date = input(
#                         "Введите новую дату выполнения задачи (день.месяц.год), или нажмите Enter для сохранения текущей): ")
#
#                     if title:
#                         tasks[task_index]['title'] = title
#                     if description:
#                         tasks[task_index]['description'] = description
#                     if date:
#                         tasks[task_index]['date'] = date
#
#                     save_tasks(tasks)
#                     print("\n" * 20)
#                     print("Задача обновлена!")
#                 else:
#                     print("\n" * 20)
#                     print("Неверный номер задачи.")
#
#             elif answer2 == "4":
#                 print("*" + "-" * 75 + "*")
#                 print(f"Сегодня {(datetime.now().strftime('%d.%m.%Y'))}. Что именно ты хочешь увидеть?")
#                 print("1. Задачи на сегодня".ljust(25), "2. Задачи на завтра".ljust(25), "3. Задачи на неделю".ljust(25))
#                 print("4. Все задачи!".ljust(25), "5. Все прошлые задачи".ljust(25), "0. Выход".ljust(25))
#                 answer3 = input("Решение: ")
#                 print("\n" * 20)
#
#
#                 if answer3 == "1":
#                     for index, task in enumerate(tasks, start=1):
#                         if task['date'] == datetime.now().strftime("%d.%m.%Y"):
#                             print(f"{index}. {task['title']} - {task['description']} (до {task['date']})")
#                     answer4 = input("Жми Enter, если рассмотрел")
#                     print("\n" * 20)
#                 elif answer3 == "2":
#                     tomorrow = datetime.now() + timedelta(days=1)
#                     for index, task in enumerate(tasks, start=1):
#                         if task['date'] == tomorrow.strftime("%d.%m.%Y"):
#                             print(f"{index}. {task['title']} - {task['description']} (до {task['date']})")
#                     answer4 = input("Жми Enter, если рассмотрел")
#                     print("\n" * 20)
#                 elif answer3 == "3":
#
#                     for index, task in enumerate(tasks, start=1):
#                         date = datetime.strptime(task['date'], "%d.%m.%Y")
#                         if (date <= (datetime.now() + timedelta(days=7)) and date >= datetime.now()):
#                             print(f"{index}. {task['title']} - {task['description']} (до {task['date']})")
#                     answer4 = input("Жми Enter, если рассмотрел")
#                     print("\n" * 20)
#                 elif answer3 == "4":
#                     for index, task in enumerate(tasks, start=1):
#                         print(f"{index}. {task['title']} - {task['description']} (до {task['date']})")
#                     answer4 = input("Жми Enter, если рассмотрел")
#                     print("\n" * 20)
#                 elif answer3 == "5":
#                     for index, task in enumerate(tasks, start=1):
#                         if datetime.strptime(task['date'], "%d.%m.%Y") < datetime.now():
#                             print(f"{index}. {task['title']} - {task['description']} (до {task['date']})")
#                     answer4 = input("Жми Enter, если рассмотрел")
#                     print("\n" * 20)
#
#                 elif answer3 == "0":
#                     continue
#
#             elif answer2 == "0":
#                 print("Всего доброго!\n")
#                 break
#     elif answer1 == "2":
#         print("Всего доброго!\n")
#
# if __name__ == "__main__":
#     main()


# import json, requests, datetime
#
# def print_weather(sity, add_to_history=False):
#     try:
#         URL = 'http://api.openweathermap.org/data/2.5/weather?q=' + sity + "&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347"
#         weather_data = requests.get(URL).json()
#         tem = weather_data['main']['temp']
#         tem_f = weather_data['main']['feels_like']
#         dis = str(weather_data['weather'][0]['description'])
#         speed = weather_data['wind']['speed']
#         print(f"Город по умолчанию: {sity}, вот данные")
#         print(f"Температура: {tem} C°; Ощущаеться как: {tem_f}C°; Скорость ветра = {speed} м/с; {dis}\n")
#         if add_to_history:
#             my_json.append([datetime.datetime.now().strftime('%d.%m.%Y %H:%M'), sity, tem, dis])
#             with open("weather_data.json", "w",encoding='utf-8') as f:
#                 json.dump(my_json, f, ensure_ascii=False,indent=4)
#
#     except KeyError:
#         print("Города нет в базе данных")
#
# print("*" + "-" * 25 + "*")
# print("|" + "Погода на седня".center(25, ' ') + "|")
# print("|" + "1.Начать".center(25, ' ') + "|")
# print("|" + "2.Выйти!".center(25, ' ') + "|")
# print("*" + "-" * 25 + "*")
# answer1 = input("Решение: ")
# print("\n" * 20)
#
# if answer1 == "1":
#
#     print("*" + "-" * 95 + "*")
#     while True:
#         with open("weather_data.json", "r", encoding='utf-8') as f:
#             my_json = json.load(f)
#
#         if my_json[0]!= "":
#             print_weather(my_json[0])
#
#         print(f"Сейчас {(datetime.datetime.now().strftime('%H:%M %d.%m.%Y'))}. Что будем делать?")
#         print("1. Узнать погоду в городе".ljust(35), "3. Просмотреть краткую историю".ljust(35))
#         print("2. Задать город по умолчанию".ljust(35), "4. Удалить всю краткую историю".ljust(35), end="")
#         print("0. Выйти")
#         answer2 = input("Решение: ")
#         print("\n" * 20)
#
#         if answer2 == "1":
#             sity = input("Введите город: ")
#             print_weather(sity, True)
#             answer3 = input("Нажмите любую клавишу, чтобы продолжить: ")
#
#         elif answer2 == "2":
#             sity = input("Введите город, который будет задаваться по умолчанию: ")
#             my_json[0] = sity
#             with open("weather_data.json", "w",encoding='utf-8') as f:
#                 json.dump(my_json, f,ensure_ascii=False,indent=4)
#
#         elif answer2 == "3":
#             histor_data = my_json[1:]
#             if len(histor_data) != 0:
#                 for i in range(0, len(histor_data)):
#                     print(str(i+1) + ". ", histor_data[i][0], histor_data[i][1], histor_data[i][2], histor_data[i][3])
#             answer3 = input("Нажмите любую клавишу, чтобы продолжить: ")
#
#         elif answer2 == "4":
#             my_json = [my_json[0]]
#             with open("weather_data.json", "w",encoding='utf-8') as f:
#                 json.dump(my_json, f,ensure_ascii=False,indent=4)
#             print("История очищена!")
#             answer3 = input("Нажмите любую клавишу, чтобы продолжить: ")
#
#         elif answer2 == "0":
#             print("Всего доброго!\n")
#             break
#         print("\n" * 20)
#
# elif answer1 == "2":
#     print("Всего доброго!\n")


