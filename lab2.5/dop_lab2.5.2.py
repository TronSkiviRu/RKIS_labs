"""Задание 2
Создайте базовый класс Animal с методом speak.
Затем создайте два подкласса Dog и Cat, которые наследуют от Animal
и переопределяют метод speak. Создайте объекты этих классов и вызовите
метод speak
"""


class Animal:
    def __init__(self):
        self.speak()

    def speak(self):
        print("Базовый голос животного")


class Dog(Animal):
    def speak(self):
        print("Гав-гав")


class Cat(Animal):
    def speak(self):
        print("Мяу-мяу")


animal1 = Animal()
dog1 = Dog()
cat1 = Cat()
