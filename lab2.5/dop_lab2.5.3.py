"""Задание 3
Создайте класс BankAccount с приватным атрибутом balance.
Реализуйте методы для депозита, снятия и проверки баланса.
Используйте методы доступа для работы с приватным атрибутом.
"""


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def check_balance(self):
        print(self.__balance, "на карте")

    def deposit(self, sum_deposit):
        self.__balance += abs(sum_deposit)
        print(self.__balance, "теперь на карте")

    def withdrawal(self, withdrawal):
        if self.__balance - abs(withdrawal) < 0:
            print("Недостаточно средств!")
            return
        self.__balance -= abs(withdrawal)
        print(self.__balance, "после списания")


acccount1 = BankAccount()
acccount1.check_balance()
acccount1.deposit(2500)
acccount1.check_balance()
acccount1.withdrawal(501)
acccount1.check_balance()

acccount2 = BankAccount()
acccount2.check_balance()
acccount2.withdrawal(-500)
acccount2.check_balance()
