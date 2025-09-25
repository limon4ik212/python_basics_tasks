a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if a < b:
    print(f"Минимум: {a}")
elif b < a:
    print(f"Минимум: {b}")
else:
    print("Числа равны")

input("Нажмите Enter для выхода...")