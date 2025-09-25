n = int(input("Введите число N: "))
fact = 1
for i in range(2, n+1):
    fact *= i
print(f"{n}! = {fact}")

input("Нажмите Enter для выхода...")