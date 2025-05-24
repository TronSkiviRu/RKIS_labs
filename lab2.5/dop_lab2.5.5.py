"""Задание 5
Евгения создала класс KgToPounds с параметром kg, куда передается
определенное количество килограмм, а с помощью метода to_pounds()
они переводятся в фунты. Чтобы закрыть доступ к переменной “kg”
она реализовала методы set_kg() - для задания нового значения
килограммов, get_kg()  - для вывода текущего значения кг.
Из-за этого возникло неудобство: нам нужно теперь использовать
эти 2 метода для задания и вывода значений.
Помогите ей переделать класс с использованием функции property()
и свойств-декораторов.
"""


class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    @property # как гетте; делает метод атрибутом
    def kg(self):
        return self.__kg

    @kg.setter # как сеттер
    def kg(self, value):
        if value < 0:
            raise ValueError("Вес не может быть отрицательным")
        self.__kg = value

    def to_pounds(self):
        return self.__kg * 2.20462


obj = KgToPounds(10)
print(obj.kg)
print(obj.to_pounds())

obj.kg = 20
print(obj.kg)
print(obj.to_pounds())