arr = list(map(int, input("Введите числа через пробел: ").split()))
x = int(input("Введите число X: "))
if x in arr:
    print("YES")
else:
    print("NO")

input("Нажмите Enter для выхода...")