import math
import random

# Task 1

a = int(input())
b = int(input())

if a % b == 0:
    print("Кратно")
else:
    print("Не кратно, остаток -> ", float(a / b))

# Task 2

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

result = math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Ратсояние между точками = ", result)

# Task 3

n = int(input())
result = len(str(n))
print(f"В числе = > {result} цифр(а/ы)")

# Task 4

list = [random.randint(-9, 9) for i in range(0, 10)]

print(list)

pl = 0
otr = 0

for i in list:
    if (i > 0):
        pl += i
    else:
        otr += i

print(f"Сумма положительных = {pl}, отрицательных = {otr}")

# Task 5

n = int(input())

b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print(b)

# Task 6

rows = int(input("Количество строк -> ")) 
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10

array = [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

for row in array:
    print(row)

for i in range(rows):
    for j in range(cols):
        if i % 2 != 0 and j % 2 != 0:
            array[i][j] = array[i][j] ** 2

print("\nМассив с нечетными индексами в квадрате:\n")
for row in array:
    print(row)

# Task 7

rows = int(input("Количество строк -> ")) 
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10

array = [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

for row in array:
    print(row)

for row in array:
    row.sort(reverse=True)

print("\nОтсартированный массив!!!\n")
for row in array:
    print(row)

# Task 8

n = int(input("Введите размерность для массива = "))

array = [[0] * n for _ in range(n)]

left, right, top, bottom = 0, n - 1, 0, n - 1
num = 1

while left <= right and top <= bottom:
    # Заполняем верхнюю границу
    for i in range(left, right + 1):
        array[top][i] = num
        num += 1

    top += 1  # Сдвигаем верхнюю границу вниз  
    
    # Заполняем правую границу
    for i in range(top, bottom + 1):
        array[i][right] = num
        num += 1

    right -= 1  # Сдвигаем правую границу влево  
    
    # Заполняем нижнюю границу
    if top <= bottom:
        for i in range(right, left - 1, -1):
            array[bottom][i] = num
            num += 1

        bottom -= 1  # Сдвигаем нижнюю границу вверъ

    # Заполняем левую границу
    if left <= right:
        for i in range(bottom, top - 1, -1):
            array[i][left] = num
            num += 1

        left += 1  # Сдвигаем левую границу вправо

for row in array:
    print(row)

# Task 9

two_numbers = list(range(10, 100))

random.shuffle(two_numbers)

depth = int(input("Количество плоскостей = "))
rows = int(input("Количество строк = "))  
cols = int(input("Количество столбцов = "))  

three_array = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(depth)]


index = 0
for i in range(depth):
    for j in range(rows):
        for z in range(cols):
            three_array[i][j][z] = two_numbers[index]
            index += 1

for i in range(depth):
    print(f"Плоскость {i}:")
    for j in range(rows):
        for z in range(cols):
            print(f"({i}, {j}, {z}) -> {three_array[i][z][j]}", end="\t")
        print() 
    print()