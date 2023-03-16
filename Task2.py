"""
Задача 2.
Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
Примеры:
1, 4, 8, 7, 5 -> 8
78, 55, 36, 90, 2 -> 90
"""
# numbers = [28, 99, 4, 40, -50]
# numMax = numbers[0]
# for i in numbers:
#     if i > numMax:
#         numMax = i
# print(numMax)

temp = []
for i in range(1, 6):
    text = f"Введите {i} число"
    temp.append(int(input(text)))
print(f"{temp} -> {max(temp)}")