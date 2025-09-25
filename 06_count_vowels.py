s = input("Введите строку: ")
vowels = "аеёиоуыэюяAEIOUaeiou"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Количество гласных:", count)

input("Нажмите Enter для выхода...")