import random

# Task 1

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10
sum = 0

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)
    
for i in range(len(random_number_list)):
    for j in range(len(random_number_list[i])):
        sum += int(random_number_list[i][j])
print("Сумма = ", sum)

# Task 2

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10
maxResult = 0

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

for i in range(len(random_number_list)):
    for j in range(len(random_number_list[i])):
        if maxResult < random_number_list[i][j]:
            maxResult = int(random_number_list[i][j])
print("Максимальный элемент = ", maxResult)

# Task 3

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10
sumer = []

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

for row in random_number_list:
    sumer.append(sum(row))

for i, row in enumerate(sumer):
    print(f"Сумма элементов строки {i + 1}: {row}")

# Task 4

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

column_sums = [0] * len(random_number_list[0])  # Инициализируем нулями

for row in random_number_list:
    for idx, value in enumerate(row):
        column_sums[idx] += value

print("Сумма элементов каждого столбца:", column_sums)

# Task 5

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)


rows = len(random_number_list)
cols = len(random_number_list[0])
transponet = [[0] * rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transponet[j][i] = random_number_list[i][j]

print("__" * 10)

for row in transponet:
    print(row)

# Task 6

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10
result = 0

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

nm = len(random_number_list)

for i in range(nm):
    result += random_number_list[i][i]

print("Сумма главной диагонали = ", result)

# Task 7

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10
sum = 0

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

for i in range(len(random_number_list)):
    for j in range(len(random_number_list[i])):
        sum += int(random_number_list[i][j])

resalt = sum / len(random_number_list)

print("Среднее значение = ", resalt)

# Task 8

list = [random.randint(0, 10) for i in range(0, 10)]
print(list)

if not list or len(list) < 3:
    print("список пустой или содержит меньше 3 элементов, невозможно найти элементы между минимальный и максимальный")
else:
    min_index = list.index(min(list))
    max_index = list.index(max(list))

    left = min(min_index, max_index) + 1
    right = max(min_index, max_index)

    if left >= right:
        print("Нету элемента между минимальным и максимальным")

    result = 1
    for i in range(left, right):
        result *= list[i]

print("Произведение элементов между минимальным и максимальным = ", result)

# Task 9

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = -10
max_value = 10

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

print("__" * 10)

for i in range(len(random_number_list)):
    for j in range(len(random_number_list[i])):
        if random_number_list[i][j] < 0:
            random_number_list[i][j] = 0

for row in random_number_list:
    print(row)

# Task 10

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

num_find = int(input("Число для поиска -> "))
list = []

for i in range(len(random_number_list)):
    for j in range(len(random_number_list[i])):
        if random_number_list[i][j] == num_find:
            list = [i, j]

if len(list) > 0:
    print(f"Первое вхождение числа {num_find} находится по индексам: {list}")
else:
    print(f"Число {num_find} не найдено в списке.")

# Task 11

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

print("__" * 10)

for i in range(len(random_number_list)):
    random_number_list[i] = random_number_list[i][::-1]

for row in random_number_list:
    print(row)

# Task 12

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 10

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

print("__" * 10)

for col in range(cols):
    column_elements = [random_number_list[row][col] for row in range(rows)]
    column_elements.reverse()
    for row in range(rows):
        random_number_list[row][col] = column_elements[row]

for row in random_number_list:
    print(row)

# Task 13

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
remove_row = int(input("Строка для удаления -> "))
min_value = 0
max_value = 10

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

print("__" * 10)

if 0 <= remove_row < len(random_number_list):
    del random_number_list[remove_row]
else:
    print("Индекс вне диапазона")

for row in random_number_list:
    print(row)

# Task 14

def generate_random_number(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

rows = int(input("Количество строк -> "))       
cols = int(input("Количество столбцов -> "))
min_value = 0
max_value = 1

random_number_list = generate_random_number(rows, cols, min_value, max_value)

for row in random_number_list:
    print(row)

max_length = 0

rows = len(random_number_list)
cols = len(random_number_list[0])

for i in range(rows):
    count = 0
    for j in range(cols):
        if random_number_list[i][j] == 0:
            count += 1
            max_length = max(max_length, count)
        else:
            count = 0

for j in range(cols):
    count = 0
    for i in range(rows):
        if random_number_list[i][j] == 0:
            count += 1
            max_length = max(max_length, count)
        else:
            count = 0

for i in range(rows):
    count = 0
    x, y = i, 0
    while x < rows and y < cols:
        if random_number_list[x][y] == 0:
            count += 1
            max_length = max(max_length, count)
        else:
            count = 0
        x += 1
        y += 1

for j in range(1, cols):
    count = 0
    x, y = 0, j
    while x < rows and y < cols:
        if random_number_list[x][y] == 0:
            count += 1
            max_length = max(max_length, count)
        else:
            count = 0
        x += 1
        y += 1

for i in range(rows):
    count = 0
    x, y = i, cols - 1
    while x < rows and y >= 0:
        if random_number_list[x][y] == 0:
            count += 1
            max_length = max(max_length, count)
        else:
            count = 0
        x += 1
        y -= 1

for j in range(cols - 2, -1, -1):
    count = 0
    x, y = 0, j
    while x < rows and y >= 0:
        if random_number_list[x][y] == 0:
            count += 1
            max_length = max(max_length, count)
        else:
            count = 0
        x += 1
        y -= 1

print(max_length)