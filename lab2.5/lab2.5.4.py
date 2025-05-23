"""Задание 4. Дана строка. Если она начинается на «abc», то замените их на «www», иначе
добавьте в конец строки «zzz»;"""
our_string = "abcxxx"
if our_string.startswith("abc"):
    print("www" + our_string[3:])
else:
    print(our_string + "zzz")