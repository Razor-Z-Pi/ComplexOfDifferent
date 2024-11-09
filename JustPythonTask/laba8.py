import random

# Task 1

list = [random.randint(0, 10) for i in range(0, 10)]

print(list)

arrayKV = []
arrayCUB = []

numK = lambda x: x ** 2
numC = lambda y: y ** 3

for i in range(0, len(list)):
    arrayKV.append([numK(list[i])])

print(*arrayKV)

for i in range(0, len(list)):
    arrayCUB.append([numC(list[i])])

print(*arrayCUB)

# Task 2

list = [random.randint(0, 10) for i in range(0, 10)]
print(list)
n = int(input("Введите число = "))

one_number = lambda x,y: x == y

print(f"Числа {one_number(n, list[0])}")    

# Task 3

n = input("Введите число = ")

is_number_str = lambda x: x.replace('.', '', 1).replace('-', '', 1).isdigit() and x.count('.') <= 1

print(f"{is_number_str(n)}")

# Task 4

list1 = [random.randint(0, 10) for i in range(0, 10)]
list2 = [random.randint(0, 10) for i in range(0, 10)]

print(list1)
print(list2)

track = list(filter(lambda x: x in list2, list1))

print(track)

# Task 5

list1 = [random.randint(0, 10) for i in range(0, 10)]
list2 = [random.randint(0, 10) for i in range(0, 10)]

print(list1)
print(list2)

track = list(map(lambda x, y: x + y, list1, list2))

print(track)

# Task 6

list1 = [random.randint(10, 100) for i in range(0, 10)]

print(list1)

result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, list1))

print(f"Числа, делящиеся на 19 или 13 = {result}")

# Task 7

list1 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

print(list1)

palindrom = lambda x: x.lower() == x[::-1].lower()

result = list(filter(palindrom, list1))

print(result)

# Task 8

list1 = [random.randint(0, 10) for i in range(0, 10)]

number = int(input("Введите число = "))

print(list1)

result = list(map(lambda x: x * number, list1))

print(result)

# Task 9

list1 = ['sally', 'DYlan', 'rebecca', 'Diana', 'Joanne', 'keith']

print(list1)

big_name = filter(lambda x: x[0].isupper(), list1)

result_length = sum(map(len, big_name))

print(result_length)

# Task 10

list1 = ['Red', 'Green', 'Blue', 'White', 'Black']

print(list1)

result = list(map(lambda x: x[::-1], list1))

print(result)