# Задание 5. Дан символ С и строковая последовательность А. Найти количество элементов
# А, которые содержат более одного символа и при этом начинаются и оканчиваются символом
# С;
def count_matching_strings(c, a):

  count = 0
  for s in a:
    if len(s) > 1 and s.startswith(c) and s.endswith(c):
      count += 1
  return count

c = "a"
a = ["apple", "banana", "apricot", "aa", "ab", "aba", "a"]
result = count_matching_strings(c, a)
print(f"Количество строк, начинающихся и заканчивающихся на '{c}': {result}")  # Вывод: 2 (aa и aba)

c = "b"
a = ["bob", "banana", "book", "bb", "b", "bab"]
result = count_matching_strings(c, a)
print(f"Количество строк, начинающихся и заканчивающихся на '{c}': {result}") # Вывод: 2 (bob и bb)

