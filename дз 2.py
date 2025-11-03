import random

numbers = []
for i in range(10):
    numbers.append(random.randint(-10, 10))

print("Исходный список:", numbers)

even = []
for x in numbers:
    if x % 2 == 0:
        even.append(x)
print("Чётные:", even)

odd = []
for x in numbers:
    if x % 2 == 1 or x % 2 == -1:
        odd.append(x)
print("Нечётные:", odd)

negative = []
for x in numbers:
    if x < 0:
        negative.append(x)
print("Отрицательные:", negative)

positive = []
for x in numbers:
    if x > 0:
        positive.append(x)
print("Положительные:", positive)