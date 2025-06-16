# Задание 5. Создать класс описывающий фитнес-центр с свойствами: Код клиента, Год,
# Номер месяца, Продолжительность занятия. Создайте список объектов класса фитнес-центр
# из 10 элементов. Определить год, в котором суммарная продолжительность занятий всех
# клиентов была наибольшей, и вывести этот год и наибольшую суммарную
# продолжительность. Если таких годов было несколько, то вывести наименьший из них;
class Fitness:
    def __init__(self, id_client, year, num_month, time_lesson):
        self.id_client = id_client
        self.year = year
        self.num_month = num_month
        self.time_lesson = time_lesson

fitness_sessions = [
    Fitness("001", 2022, 5, 60),
    Fitness("002", 2001, 6, 65),
    Fitness("003", 2011, 7, 930),
    Fitness("004", 2033, 8, 3330),
    Fitness("005", 2012, 5, 230),
    Fitness("006", 2022, 4, 323),
    Fitness("007", 2001, 4, 3300),
    Fitness("009", 2011, 2, 93),
    Fitness("010", 2033, 3, 30),
    Fitness("011", 2012, 1, 2030)
]

year_dict = dict()
for session in fitness_sessions:
    if session.year not in year_dict:
        year_dict[session.year] = session.time_lesson
    else:
        year_dict[session.year] += session.time_lesson

max_duration = max(year_dict.values())
print(max_duration)
max_years = [year for year, duration in year_dict.items() if duration == max_duration]
result_year = min(max_years) if max_years else None

print(f"Год с наибольшей суммарной продолжительностью занятий: {result_year}")
print(f"Суммарная продолжительность: {max_duration} минут")
