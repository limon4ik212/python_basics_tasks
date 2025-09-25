import runpy

tasks = [
    "01_min_of_two.py",
    "02_even_or_odd.py",
    "03_sum_1_to_n.py",
    "04_multiplication_table.py",
    "05_factorial_loop.py",
    "06_count_vowels.py",
    "07_reverse_string.py",
    "08_max_in_array.py",
    "09_sum_array.py",
    "10_contains_x.py",
]

while True:
    print("\nМеню задач:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")
    print("0. Выход")

    choice = input("Выберите номер задачи: ")
    if choice == "0":
        break
    if choice.isdigit() and 1 <= int(choice) <= len(tasks):
        runpy.run_path(tasks[int(choice) - 1])
        input("\nНажмите Enter, чтобы вернуться в меню...")
