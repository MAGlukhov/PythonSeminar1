"""
Задача 1.
Написать программу, которая принимает на вход два целых числа и проверяет, является ли одно число квадратом другого.
Примеры
5, 25 -> да
4, 16 -> да
25, 5 -> да
8,9 -> нет

1. Понять смысл задания
2. Разбираемся с входом и выходом данных
3. Алгоритм (псевдокод!)
4. Записать код
5. Проверить код
6. Улучшить код (деаакторинг)
7* Оптимизация (зависит от требований)
"""

a=input("Введите число а: ")
b=input("Введите число b: ")

while not a.isdigit() or not b.isdigit():
    a = input("Введите число а: ")
    b = input("Введите число b: ")

if int(a)==int(b)**2 or int(b)==int(a)**2:
    print("Да")
else:
    print("Нет")
