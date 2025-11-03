import random

numbers = []
for i in range(10):
    num = random.randint(-10, 10)
    numbers.append(num)

print("Наш список:", numbers)

sum_negative = 0
for num in numbers:
    if num < 0:
        sum_negative = sum_negative + num
print("1. Сумма отрицательных чисел =", sum_negative)

sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even = sum_even + num
print("2. Сумма чётных чисел =", sum_even)

sum_odd = 0
for num in numbers:
    if num % 2 != 0:
        sum_odd = sum_odd + num
print("3. Сумма нечётных чисел =", sum_odd)

product = 1
for i in range(len(numbers)):
    if i % 3 == 0:
        product = product * numbers[i]
print("4. Произведение элементов с индексами кратными 3 =", product)

min_num = numbers[0]
min_index = 0
for i in range(len(numbers)):
    if numbers[i] < min_num:
        min_num = numbers[i]
        min_index = i

max_num = numbers[0]
max_index = 0
for i in range(len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        max_index = i

if min_index < max_index:
    start = min_index
    end = max_index
else:
    start = max_index
    end = min_index

result = 1
for i in range(start + 1, end):
    result = result * numbers[i]
print("5. Произведение между min и max =", result)

first_positive = -1
for i in range(len(numbers)):
    if numbers[i] > 0:
        first_positive = i
        break

last_positive = -1
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] > 0:
        last_positive = i
        break

sum_between = 0
if first_positive != -1 and last_positive != -1:
    if first_positive < last_positive:
        for i in range(first_positive + 1, last_positive):
            sum_between = sum_between + numbers[i]
    else:
        for i in range(last_positive + 1, first_positive):
            sum_between = sum_between + numbers[i]

print("6. Сумма между первым и последним положительными =", sum_between)