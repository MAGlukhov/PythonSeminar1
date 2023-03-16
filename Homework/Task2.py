"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
x = True
y = False
z = True

first = not (x or y or z)
second = not x and not y and not z

print(first == second)