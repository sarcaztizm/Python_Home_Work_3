# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random

N = int(input('Введите число N: '))
numbers = []

for i in range(N):
    numbers.append((random.randint(0, 10)))
print(numbers)

X = int(input('Введите заданное число X: '))

difference = abs(X - numbers[0])
result = numbers[0]

for i in range(1, len(numbers)-1):
    if difference >= abs(numbers[i] - X):
        difference = abs(numbers[i] - X)
        result = numbers[i]

print(result)