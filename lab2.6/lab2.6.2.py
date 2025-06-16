# Задание 2. Создайте класс User с свойствами Login и Password. Создайте список объектов
# User из 5 элементов. Выведите из этого списка пользователя с определенными логином и
# паролем;
class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
users_arr = [User("gr_632", "1qazxsw23edc"),
             User("gr_632", "kw9d0wjd9x"),
             User("gr_932", "askixj8wxdac"),
             User("gr_732", "asdszxswex"),
             User("gr_432", "1wdwxsw23edc"),]
for user in users_arr:
    if user.login == "gr_432" and user.password == "1wdwxsw23edc":
        print(user.login, " -- ", user.password)
