"""Задание 1
Создайте простой класс Car, который будет представлять автомобиль.
Класс должен иметь атрибуты для марки, модели и года выпуска автомобиля.
Затем создайте объект этого класса и выведите его атрибуты на экран

"""


class Car:
    def __init__(self, brand, model, year_release):
        self.brand = brand
        self.model = model
        self.year_release = year_release
        print(f"Создан {model} {brand}, {year_release} года выпуска")


tesla_car = Car("XT", "Tesla", 2023)
