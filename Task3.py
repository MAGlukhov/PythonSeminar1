"""
Задача 3.
Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
Примеры:
5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
"""
number = int(input("Введите число "))
i = -number
answer = str(number) + " -> "
while i <= number:
    answer = answer + str(i) + " "
    i = i + 1
print(answer)