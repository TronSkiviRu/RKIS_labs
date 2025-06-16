# Дана строковая последовательность. Найти сумму длин всех строк, входящих в
# данную последовательность;
string_sequence = ["apple", "banana", "cherry"]
total_length = sum(len(word) for word in string_sequence)
print(f"Сумма длин всех строк: {total_length}")