# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

import random

N = int(input('Введите число N: '))
numbers = []

for i in range(N):
    numbers.append((random.randint(0, 10)))
print(numbers)

find_number = int(input('Введите число для поиска: '))
count = 0

for i in range(N):
    if (numbers[i] == find_number):
        count += 1

print(count)
