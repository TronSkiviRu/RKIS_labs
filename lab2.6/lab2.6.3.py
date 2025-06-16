# Задание 3. Создайте класс Task описывающий занятие, с свойствами: DateStart, DateFinish,
# Description. Создайте список объектов Task из 5 элементов. Выведите информацию о занятии
# заканчивающемся позже всех, если таких занятий несколько, выведите первое подходящее
# под условие;
class Task:
    def __init__(self, dateStart, dateFinish, description):
        self.dateStart = dateStart
        self.dateFinish = dateFinish
        self.description = description
    def __lt__(self, other):
        return self.dateStart < other.dateStart
array_tasks = [Task((2025, 6, 10, "10:00"), (2025, 6, 10, "16:00"), "webDev"),
                Task((2025, 6, 12, "6:00"), (2025, 6, 12, "10:00"), "webDev"),
                Task((2025, 6, 13, "10:00"), (2025, 6, 13, "16:00"), "GameDev"),
                Task((2025, 6, 14, "6:00"), (2025, 6, 14, "10:00"), "StereoDev"),
                Task((2025, 6, 15, "10:00"), (2025, 6, 15, "16:00"), "GameDev")
               ]
array_tasks.sort(reverse=True)
print(array_tasks[0].dateStart, " : ", array_tasks[0].dateFinish, " -- ", array_tasks[0].description)
