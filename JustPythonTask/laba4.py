import random
from collections import Counter

# Task 1
list = [random.randint(-10, 10) for i in range(0, 10)]
sum = 0

print(list)

for i in range(0, 9):
    if list[i] >= 0 and list[i] % 2 == 0:
        sum += list[i]

print("Сумма положительных и четных чисел: ", sum)

# Task 2
list = [random.randint(1, 10) for i in range(0, 10)]
result = 0
print(list)

for i in range(0, 10):
    if i > 0 and i % 2 == 0:
        if result < list[i]:
            result = list[i]

print("Максимальный элемент среди четных индексов: ", result)

# Task 3
list = [random.randint(1, 10) for i in range(0, 10)]
sum = 0
average = 0

print(list)

for i in range(0, 10):
    sum += list[i]

average = sum / len(list)

for i in range(0, 10):
    if average > list[i]:
        print("Меньше средне арифметического числа:", average, " > ", list[i])

# Task 4
list = [random.randint(1, 10) for i in range(0, 10)]
print(list)

min_1 = list[0]
min_2 = list[0]

for i in list:
    if i < min_1:
        min_1 = i

if list.count(min_1) == 1:
    for i in list:
      if i < min_2 and i != min_1:
           min_2 = i
else:
    min_2 = min_1

print('Самый маленький элемент массива: {}. Следующий самый маленький элемент: {}'.format(min_1, min_2))

# Task 5
list = [random.randint(-10, 10) for i in range(0, 10)]
print(list)

neg = -1

for i in range(0, 10):
    if list[i] < 0:
        neg = i
        break

if neg == -1:
    print('Отрицательных нет')
else:
    print('Номер первого отрицательно числа:', neg+1)
    s = 0
    for i in range(neg+1,10):
        s += abs(list[i])
    print('Сумма: ', s)

# Task 6
list = [random.randint(-10, 10) for i in range(0, 10)]
print(list)

n = 0

for i in range(0, 10):
    if abs(list[i]) < abs(list[n]):
        n = i

print(n)

# Task 7
arr = [random.randint(11, 101) for i in range(0, 4)]
tmp = []

print(arr)

for i in arr:
    tmp.append(str(i))
print(sum(map(int, list(''.join(tmp)))))

# Task 8
arr = [random.randint(1, 10) for i in range(0, 10)]
print(arr)

mn = min(arr)
mx = max(arr)

print('min: ', mn)
print('max: ', mx)

summex = sum(arr[min(arr.index(mn), arr.index(mx)) + 1:max(arr.index(mn), arr.index(mx))])
print(summex)

# Task 9
list = [random.randint(-10, 10) for i in range(0, 10)]
print(list)
minmax = 0
index = 0

for i in range(0, 10):
    if minmax > list[i]:
        minmax = list[i]
        index = i

print(index, " - ", minmax)

# Task 10
list = [random.randint(-10, 10) for i in range(0, 10)]
print(list)
print(max(list, key=list.count))

# Task 11
list = [random.randint(-10, 10) for i in range(0, 10)]
print(list)

maximum = max(list)
minimum = min(list)

for i in range(0, 10):
  if list[i] == maximum:
    list[i] = minimum
  elif list[i] == minimum:
    list[i] = maximum
 
print(list)

# Task 12
list = [random.randint(-10, 10) for i in range(0, 10)]
print(list)
counter = Counter(list)
unique_elements = [item for item, count in counter.items() if count == 1]
print(unique_elements)

# Task 13
list = [random.randint(-10, 10) for i in range(0, 10)]
print(list)
list.reverse()
print(list)

# Task 14
list = [random.randint(1, 10) for i in range(0, 10)]
print(list)

sum_of_numbers = sum(list)

n = 1

for i in range(0, 10):
    n *= list[i]

print("Сумма элементов:", sum_of_numbers)
print("Произведение элементов:", n)