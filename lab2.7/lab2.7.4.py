# Задание 4. Создать класс описывающий фитнес-центр с свойствами: Код клиента, Год,
# Номер месяца, Продолжительность занятия. Создайте список объектов класса фитнес-центр
# из 5 элементов. Вывести информацию о самом продолжительном и самом коротком занятиях;
class Fitness:
    def __init__(self, id_client, year, num_month, time_lesson):
        self.id_client = id_client
        self.year = year
        self.num_month = num_month
        self.time_lesson = time_lesson

    def __str__(self):
        return (f"Клиент: {self.id_client}, Год: {self.year}, "
                f"Месяц: {self.num_month}, Продолжительность: {self.time_lesson} мин.")

fitness_sessions = [
    Fitness("001", 2022, 5, 60),
    Fitness("002", 2001, 6, 65),
    Fitness("003", 2011, 7, 930),
    Fitness("007", 2033, 8, 3330),
    Fitness("005", 2012, 9, 230)
]
long_session = max(fitness_sessions, key=lambda x: x.time_lesson)
short_session = min(fitness_sessions, key=lambda x: x.time_lesson)

print(long_session)
print(short_session)